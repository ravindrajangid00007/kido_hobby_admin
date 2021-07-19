from ..models import db
from datetime import datetime

class Batches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch_size = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer , nullable=False)
    batch_start = db.Column(db.DateTime , nullable=False)
    batch_end = db.Column(db.DateTime , nullable=False)
    confirmed_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    courses = db.relationship('Courses', secondary='batches_courses' ,backref=db.backref('batches', lazy=True))

    