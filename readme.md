# Hospital Appointment Management System

A **web-based hospital appointment management system** for clinicians to manage NCD (Non-Communicable Disease) patients. Built using **Python Flask, MySQL, HTML/CSS, Bootstrap**, with email notifications and logging for patient appointments.

---

## Features

- Clinician registration and login (with secure hashed passwords)
- Add, edit, delete, and search patient records
- Track patient next appointment dates
- Automatic email reminders for upcoming appointments
- Logging of all actions (login, CRUD operations)
- Responsive dashboard and forms using Bootstrap
- Easy to extend with additional patient fields or notifications

---

## Technologies Used

- **Backend:** Python 3, Flask, Flask-Login, Flask-SQLAlchemy
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap 5
- **Email Notifications:** Flask-Mail (SMTP)
- **Task Scheduler:** APScheduler
- **Logging:** Python logging module

---

## Project Structure

BOOKINGAPPOINTMENT_NCD/ <br>
│<br>
├── __pycache__/                 # Compiled Python cache files <br>
│
├── logs/
│   └── app.log                  # Application log file
│
├── ncd/                         # Virtual environment directory (venv)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── static/
│   └── css/
│       └── style.css            # Custom stylesheet
│
├── templates/                   # HTML templates for Flask
│   ├── base.html                # Base layout shared by all pages
│   ├── dashboard.html           # Dashboard page
│   ├── login.html               # Login page
│   ├── patient_form.html        # Patient registration form
│   ├── patient_list.html        # Patient list page
│   ├── register.html            # User registration page
│   └── welcome.html             # Home/landing page
│
├── app.py                       # Main Flask application entry point
├── config.py                    # Application configuration settings
├── models.py                    # Database models
├── routes.py                    # Application route definitions
├── utils.py                     # Utility/helper functions
│
├── requirements.txt             # Python dependencies
└── readme.md                    # Project documentation


