from flask import Flask , request ,Blueprint ,render_template,flash
from werkzeug.utils import redirect

admin_route = Blueprint('admin' , __name__)

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
        
        return render_template('adminDashboard.html')


@admin_route.route('/addTeacher' , methods=['GET','POST'])
def addTeacher():
    if request.method == 'GET':
        return render_template('addTeacher.html')

@admin_route.route('/addCourse')
def addCourse():
    return render_template('addCourse.html')


