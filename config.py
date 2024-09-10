import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://water_user:postgresql@localhost/water_treatment_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
