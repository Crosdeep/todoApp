import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PpODdfeVgfK'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:pp123@localhost/todo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

