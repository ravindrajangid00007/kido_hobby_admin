from admin_panal.models import db

class Course(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     coursename = db.Column(db.String, nullable=False)
     courseprice = db.Column(db.Float, nullable=False)
     coursecode=db.column(db.Text, nullable=False)
     coursediscription=db.Column(db.Text,nullable=False)
     coursebroucher = db.Column(db.File,nullable=False)





# coursename
# courscode
# coursediscription
# coursebroucher
# coursevideolink
# thumbnailimageurl
# imagelink1
# imagelink2
# noofclasses
# mon
# tue
# wed
# courseduration
# coursetype
# coursecategory
# tag
# minage
# maxage
# price