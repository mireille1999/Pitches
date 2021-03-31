import os

class Config:
    """
    General configuration parent class
    """
    #pass
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL?sslmode=require')
    

class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mireille:potatopeel420@localhost/pitches'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}