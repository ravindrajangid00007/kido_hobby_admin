from ..models import db
from datetime import datetime
class Course(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(30), nullable=False)
     author=db.Column(db.String(30), nullable=False)
     category=db.Column(db.String(30), nullable=False)
     discription=db.Column(db.Text,nullable=False)
     broucher = db.Column(db.LargeBinary,nullable=False)
     coursevideolink = db.Column(db.String(120), nullable=False)
     thumbnailimage= db.Column(db.LargeBinary, nullable=False)
     videoimage1=db.Column(db.LargeBinary, nullable=False)
     videoimage2=db.Column(db.LargeBinary,nullable=False)
     noofclasses=db.Column(db.Integer,nullable=False)
     weekday=db.Column(db.String(30),nullable=False)
     duration=db.Column(db.String(30), nullable=False)
     coursetype=db.Column(db.String(30), nullable=False)
     minage=db.Column(db.Integer, nullable=False)
     maxage=db.Column(db.Integer, nullable=False)
     price=db.Column(db.Float, nullable=False)
     state=db.Column(db.String(30), nullable=False)
     adminname=db.Column(db.String(30),nullable=False)
     adddate=db.Column(db.DateTime,nullable=False)
     modifieddate=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  
     

     def __repr__(self):
         return f"Course('{self.id}','{self.name}','{self.price}','{self.state}')"
