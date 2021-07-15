import functools
from flask import Flask , request ,Blueprint ,render_template, flash, session, url_for, g
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash

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
        return redirect(url_for('admin.adminDashboard'))

#Logout feature

@admin_route.route('/logout')
def logout():
    session.clear()
    print(g.user)
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

@admin_route.route('/addCourse',methods=["GET","POST"])
def addCourse():
    if (request.method == "POST"):
        data=request.form
        print(data)
        return render_template('addCourse.html')
    return render_template('addCourse.html')


