import urllib.parse

class Config:
    SECRET_KEY = '6ee9f69830f1589116fb9b96863ed8fa'

    # Database settings
    DB_USER = 'root'
    DB_PASSWORD = 'Mysql$michu12'  # replace with your MySQL password
    DB_HOST = 'localhost'
    DB_NAME = 'hospital_db'

    # Properly URL-encode the password
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{urllib.parse.quote_plus(DB_PASSWORD)}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'moketchus12@gmail.com'
    MAIL_PASSWORD = 'ibhz finv zoak rvnv'
