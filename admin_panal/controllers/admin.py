from datetime import datetime
import functools
from os import error
from flask import Flask , request ,Blueprint ,render_template, flash, session, url_for, g
from sqlalchemy.orm import query
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import db
from ..models.course import Course
from ..models.teachers import Teacher

admin_route = Blueprint('admin' , __name__)



# Login feature

@admin_route.route('/' , methods=['GET','POST'])
def adminLogin():
    if request.method == 'GET':
        return render_template('adminLogin.html')
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email.upper() != 'ADMIN@ADMIN.COM':
            flash("incorrect email!")
            return render_template('adminLogin.html')
        if password != 'hello@admin':
            flash("incorrect password!")
            return render_template('adminLogin.html')
        
        session.clear()
        session['user_id'] = 'ADMIN'
        print(url_for('admin.adminDashboard'))
        return redirect(url_for('admin.adminDashboard'))

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
    return render_template('adminDashboard.html')


@admin_route.route('/addTeacher' , methods=['GET','POST'])
@login_required
def addTeacher():
    if request.method == 'GET':
        return render_template('addTeacher.html')

    if request.method == 'POST':
        data = request.form.to_dict()
        
        same_username = Teacher.query.filter_by(username = data['username'].upper())
        same_email = Teacher.query.filter_by(email = data['email'].upper())
        error = None
        
        if same_username.first() != None:
            error = "Username already exists"
        elif same_email.first() != None:
            error = "Email already exists"

        if error is None:
            data['password'] = generate_password_hash(data['password'], method='pbkdf2:sha256', salt_length=16)
            data['username'] = data['username'].upper()
            data['email'] = data['email'].upper()

            newTeacher = Teacher(**data)
            try:

                db.session.add(newTeacher)
                db.session.commit()
                flash("success")
                return redirect(url_for("admin.addTeacher"))
            except:
                return "Bad Request",400
        
        flash(error)
        return redirect(url_for("admin.addTeacher"))    
    

@admin_route.route('/addCourse',methods=["GET","POST"])
@login_required
def addCourse():
    if (request.method == "POST"):
        try:
                data=request.form.to_dict() 
                print(data)
                weekday=" ".join(request.form.getlist('weekday'))
                broucher=request.files['broucher'].read() 
                video=request.files['video'].read() 
                thumbnailimage=request.files['thumbnailimage'].read() 
                videoimage1=request.files['videoimage1'].read() 
                videoimage2=request.files['videoimage2'].read() 
                course=Course(name=data['name'],              
                            author=data['author'],
                            category=data['category'],
                            discription=data['discription'],
                            broucher=broucher,
                            video=video,
                            thumbnailimage=thumbnailimage,
                            videoimage1=videoimage1,
                            videoimage2=videoimage2,
                            noofclasses=data['noofclasses'],
                            weekday=weekday,
                            duration=data['duration'],
                            coursetype=data['coursetype'],
                            minage=int(data['minage']),
                            maxage=int(data['maxage']),
                            price=float(data['price']),
                            state=data['state'],
                            adminname=g.user,
                            adddate=datetime.utcnow(),
                            )
                db.session.add(course)
                db.session.commit()
                flash("success")
                return redirect(url_for("admin.addCourse"))
        except Exception as e:
                print(e)
                flash("error")
                return redirect(url_for("admin.addCourse"))
    return render_template('addCourse.html')




@admin_route.route('/getCourse',methods=['GET','POST'])
@login_required
def getCourse():
    if (request.method=='POST'):
        print("post")
    return render_template('getCourse.html')


