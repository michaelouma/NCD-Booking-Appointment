from flask import Flask
from config import Config
from models import db, Clinician
from flask_login import LoginManager
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler

login_manager = LoginManager()
login_manager.login_view = 'routes.login'
mail = Mail()
scheduler = BackgroundScheduler()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from routes import routes_blueprint, check_appointments
    app.register_blueprint(routes_blueprint)

    scheduler.add_job(func=lambda: check_appointments(app, mail), trigger="interval", hours=24)
    scheduler.start()

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return Clinician.query.get(int(user_id))

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # create tables if they don't exist
    app.run(debug=True)
