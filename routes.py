from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import Clinician, Patient, db

main = Blueprint('main', __name__)

# -------------------------
# HOME / WELCOME
# -------------------------
@main.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('welcome.html', active_page="home")

# -------------------------
# DASHBOARD
# -------------------------
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', active_page="dashboard")

# -------------------------
# REGISTER CLINICIAN
# -------------------------
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if Clinician.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for('main.register'))

        user = Clinician(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect(url_for('main.login'))

    return render_template('register.html', active_page="register")

# -------------------------
# LOGIN
# -------------------------
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Clinician.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))

        flash("Invalid username or password")
        return redirect(url_for('main.login'))

    return render_template('login.html', active_page="login")

# -------------------------
# LOGOUT
# -------------------------
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('main.home'))

# -------------------------
# PATIENT LIST
# -------------------------
@main.route('/patients')
@login_required
def patients():
    search = request.args.get('search', '')

    if search:
        patients = Patient.query.filter(Patient.fullname.ilike(f'%{search}%')).all()
    else:
        patients = Patient.query.all()

    return render_template('patients.html', patients=patients, active_page="patients")

# -------------------------
# ADD PATIENT
# -------------------------
@main.route('/add_patient', methods=['GET', 'POST'])
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

        flash("Patient added successfully")
        return redirect(url_for('main.patients'))

    return render_template('patient_form.html', patient=None, active_page="register_patient")

# -------------------------
# EDIT PATIENT
# -------------------------
@main.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
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

        flash("Patient updated successfully")
        return redirect(url_for('main.patients'))

    return render_template('patient_form.html', patient=patient, active_page="patients")

# -------------------------
# DELETE PATIENT
# -------------------------
@main.route('/delete_patient/<int:id>', methods=['POST'])
@login_required
def delete_patient(id):
    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    flash("Patient deleted successfully")
    return redirect(url_for('main.patients'))


# ======================================================
# NEWLY ADDED ROUTES TO FIX BuildError
# ======================================================

# -------------------------
# APPOINTMENTS PAGE (Fixes sidebar error)
# -------------------------
@main.route('/appointments')
@login_required
def appointments():
    return render_template('appointments.html', active_page="appointments")

# -------------------------
# REPORTS PAGE (Fixes sidebar error)
# -------------------------
@main.route('/reports')
@login_required
def reports():
    return render_template('reports.html', active_page="reports")
