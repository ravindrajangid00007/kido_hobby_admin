from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms import TextField, PasswordField ,SelectField
from wtforms.fields.core import BooleanField, IntegerField
from wtforms.validators import InputRequired, Email, DataRequired


class addTeacherForm(FlaskForm):
    Firstname = TextField('Firstname'     , id='firstname_create' , validators=[DataRequired()])
    Lastname =  TextField('Lastname'      , id='lastname_create'  , validators=[])
    email =     TextField('Email'         , id='email_login'      , validators=[DataRequired(),Email()])
    age =       IntegerField('Age'        , id='age'              , validators=[DataRequired()])
    password =  PasswordField('Password'  , id='pwd_login'        , validators=[DataRequired()])
    is_teacher = BooleanField('Teacher'   , render_kw={'value': 1})  
    skills = SelectField('Skills' ,coerce=int)
