import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_password'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://kisi:pp123@localhost/todo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

