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
├── __pycache__/            # Compiled Python cache files <br>
│<br>
├── logs/<br>
│   └── app.log                  # Application log file<br>
│<br>
├── ncd/                         # Virtual environment directory (venv)<br>
│   ├── Include/<br>
│   ├── Lib/<br>
│   ├── Scripts/<br>
│   └── pyvenv.cfg<br>
│<br>
├── static/<br>
│   └── css/<br>
│       └── style.css <br>
└── images/<br>
│       └── img.jpg <br>
│<br>
├── templates/                   # HTML templates for Flask<br>
│   ├── base.html                # Base layout shared by all pages<br>
│   ├── dashboard.html           # Dashboard page<br>
│   ├── login.html               # Login page<br>
│   ├── patient_form.html        # Patient registration form<br>
│   ├── patient_list.html        # Patient list page<br>
│   ├── register.html            # User registration page<br>
│   └── welcome.html             # Home/landing page<br>
│<br>
├── app.py                       # Main Flask application entry point<br>
├── config.py                    # Application configuration settings<br>
├── models.py                    # Database models<br>
├── routes.py                    # Application route definitions<br>
├── utils.py                     # Utility/helper functions<br>
│<br>
├── requirements.txt             # Python dependencies<br>
└── readme.md                    # Project documentation


