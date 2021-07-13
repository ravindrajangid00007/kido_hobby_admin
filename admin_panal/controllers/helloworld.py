from flask import Flask , request ,Blueprint ,render_template

helloworld_route = Blueprint('helloworld' , __name__)

@helloworld_route.route('/' , methods=['GET'])
def helloworld():
    return render_template('helloworld.html')
