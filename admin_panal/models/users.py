from ..models import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean , nullable=False , default=False)
    is_teacher = db.Column(db.Boolean , nullable=False , default=False)
    confirmed_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    batches = db.relationship('Batches', secondary='users_batches' ,backref=db.backref('users', lazy=True))
    skills = db.relationship('Skills', secondary='users_skills' ,backref=db.backref('users', lazy=True))
    