from ..models import db
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class Course(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(30), nullable=False)
     author=db.Column(db.String(30), nullable=False)
     category=db.Column(db.String(30), nullable=False)
     discription=db.Column(db.Text,nullable=False)
     broucher = db.Column(db.LargeBinary,nullable=False)
     video = db.Column(db.LargeBinary, nullable=False)
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



class addcourse(FlaskForm):
    course_name = StringField('Course Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add Course')
