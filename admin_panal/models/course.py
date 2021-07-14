from admin_panal.models import db

class Course(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     coursename = db.Column(db.String, nullable=False)
     courseprice = db.Column(db.Float, nullable=False)
     