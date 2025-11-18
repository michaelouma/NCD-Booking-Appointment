import logging
from flask_mail import Message

# Logging setup
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(action):
    logging.info(action)

def send_email_reminder(patient, clinician_email, mail, app):
    """Send email reminder using Flask-Mail."""
    with app.app_context():
        msg = Message(
            subject=f"Appointment Reminder: {patient.fullname}",
            recipients=[clinician_email],
            body=f"Patient {patient.fullname} has an appointment tomorrow ({patient.next_appointment})."
        )
        mail.send(msg)
        log_action(f"Reminder sent for patient {patient.fullname} to {clinician_email}")
