import functools
from os import error, name
from flask import Flask , request ,Blueprint ,render_template, flash, session, url_for, g
from sqlalchemy.orm import query
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import db
from ..models.users import Users
from ..models.batches import Batches
from ..models.courses import Courses
from ..models import *
from ..forms.loginForm import LoginForm
from ..forms.teacherForm import addTeacherForm


admin_route = Blueprint('admin' , __name__)

# Login feature

@admin_route.route('/' , methods=['GET','POST'])
def adminLogin():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('accounts/adminLogin.html', form=form)
        
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(email=username).first()
           
        if user and check_password_hash(user['password'], password) and form.validate_on_submit():        
            session.clear()
            #storing user_id in the session
            #it will be used to check if admin is logged in
            session['user_id'] = user.id
            return redirect(url_for('admin.adminDashboard'))
        
        return render_template( 'accounts/adminLogin.html', msg='Wrong user or password', form=form)


#Logout feature

@admin_route.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.adminLogin'))


# checks if a user id is stored in the session

@admin_route.before_app_request
def load_logged_in_user():
    user = session.get('user_id')
    if user is None:
        g.user = None
    else:
        g.user = 'ADMIN'

# This function will check if user is logged in or not

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Login required")
            return redirect(url_for('admin.adminLogin'))

        return view(**kwargs)

    return wrapped_view



@admin_route.route('/dashboard')
@login_required
def adminDashboard():
    return render_template('home/adminDashboard.html')


@admin_route.route('/addTeacher' , methods=['GET','POST'])
@login_required
def addTeacher():
    teacherForm = addTeacherForm()

    if request.method == 'GET':
        return render_template('home/addTeacher.html',form=teacherForm)

    if request.method == 'POST':
        
        data = request.form.to_dict()
        
            


@admin_route.route('/getTeacher/',methods=['GET','POST'])
@login_required
def getTeacher():
    teachers = []
    if request.method =='POST':
        name = request.form
        search = "%{}%".format(name['searchValue'])
        teachers = Users.query.filter(Users.firstname.like(search) and Users.is_teacher==1).all()
        if not teachers:
           flash("No Teacher Found") 
        return render_template('getTeacher.html',teachers=teachers)
    return render_template('getTeacher.html',teachers=teachers)



@admin_route.route('/addCourse',methods=["GET","POST"])
@login_required
def addCourse():
    if (request.method == "POST"):
        data=request.form
        print(data)
        return render_template('addCourse.html')
    return render_template('addCourse.html')


