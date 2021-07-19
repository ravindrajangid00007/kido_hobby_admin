from ..models import db
from datetime import datetime

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(80), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    courses = db.relationship('Courses', backref='skill', lazy=True)