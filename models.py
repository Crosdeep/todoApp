#models
from email.policy import default

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import nulls_last

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    task = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f'Todo {self.title}'
