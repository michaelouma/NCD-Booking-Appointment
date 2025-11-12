from flask import render_template, redirect, url_for, request, flash
from app import app, db, login_manager
from models import Clinician, Patient
from flask_login import login_user, logout_user, login_required, current_user
from utils import log_action, send_email_reminder
from datetime import date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

@login_manager.user_loader
def load_user(user_id):
    return Clinician.query.get(int(user_id))

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if Clinician.query.filter_by(username=username).first():
            flash("Username already exists")
        else:
            clinician = Clinician(username=username, email=email)
            clinician.set_password(password)
            db.session.add(clinician)
            db.session.commit()
            log_action(f"New clinician registered: {username}")
            flash("Registration successful! Please login.")
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Clinician.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            log_action(f"{username} logged in")
            return redirect(url_for('dashboard'))
        flash("Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    log_action(f"{current_user.username} logged out")
    logout_user()
    return redirect(url_for('login'))

@app.route('/patients')
@login_required
def patients():
    search = request.args.get('search', '')
    patients = Patient.query.filter(Patient.fullname.like(f'%{search}%')).all()
    return render_template('patient_list.html', patients=patients)

@app.route('/patients/add', methods=['GET','POST'])
@login_required
def add_patient():
    if request.method == 'POST':
        patient = Patient(
            fullname=request.form['fullname'],
            contact=request.form['contact'],
            disease=request.form['disease'],
            next_appointment=request.form['next_appointment'],
            other_details=request.form['other_details']
        )
        db.session.add(patient)
        db.session.commit()
        log_action(f"Added patient: {patient.fullname}")
        flash("Patient added successfully")
        return redirect(url_for('patients'))
    return render_template('patient_form.html', patient=None)

@app.route('/patients/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        patient.fullname = request.form['fullname']
        patient.contact = request.form['contact']
        patient.disease = request.form['disease']
        patient.next_appointment = request.form['next_appointment']
        patient.other_details = request.form['other_details']
        db.session.commit()
        log_action(f"Edited patient: {patient.fullname}")
        flash("Patient updated successfully")
        return redirect(url_for('patients'))
    return render_template('patient_form.html', patient=patient)

@app.route('/patients/delete/<int:id>', methods=['POST'])
@login_required
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    log_action(f"Deleted patient: {patient.fullname}")
    flash("Patient deleted successfully")
    return redirect(url_for('patients'))

def check_appointments():
    tomorrow = date.today() + timedelta(days=1)
    patients = Patient.query.filter_by(next_appointment=tomorrow).all()
    for patient in patients:
        send_email_reminder(patient, current_user.email)

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_appointments, trigger="interval", hours=24)
scheduler.start()
