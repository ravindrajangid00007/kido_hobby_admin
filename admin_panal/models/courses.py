from ..models import db
from datetime import datetime

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80), unique=False, nullable=False)
    course_code = db.Column(db.String(80), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    update_at = db.Column(db.DateTime, nullable=False,default= datetime.utcnow)
    skill_fk = db.Column(db.Integer, db.ForeignKey('skills.id'),nullable=False)
    