from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import Clinician, Patient, db
from utils import send_email_reminder
from datetime import date, timedelta

routes_blueprint = Blueprint('routes', __name__)

# Example: home route
@routes_blueprint.route('/')
def home():
    return "Welcome to Hospital Appointment System"

# Clinician login route
@routes_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        clinician = Clinician.query.filter_by(username=username).first()
        if clinician and clinician.check_password(password):
            login_user(clinician)
            return redirect(url_for('routes.home'))
        flash('Invalid username or password')
    return render_template('login.html')

@routes_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

# Scheduler function to check tomorrow's appointments
def check_appointments(app, mail):
    with app.app_context():
        tomorrow = date.today() + timedelta(days=1)
        patients = Patient.query.filter_by(next_appointment=tomorrow).all()
        for patient in patients:
            clinician_email = 'clinician@example.com'  # replace with actual clinician email
            send_email_reminder(patient, clinician_email, mail, app)
