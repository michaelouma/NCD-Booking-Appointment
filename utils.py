import logging
from flask_mail import Message
from app import mail, app

# Logging setup
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(action):
    logging.info(action)

# Send email reminder
def send_email_reminder(patient, clinician_email):
    with app.app_context():
        msg = Message(
            subject=f"Appointment Reminder: {patient.fullname}",
            recipients=[clinician_email],
            body=f"Patient {patient.fullname} has an appointment tomorrow ({patient.next_appointment})."
        )
        mail.send(msg)
        log_action(f"Reminder sent for patient {patient.fullname} to {clinician_email}")
