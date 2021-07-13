from flask import Flask

#data base object 
from .models import db

#blueprints
from .controllers.helloworld import helloworld_route


def create_app():
    app = Flask(__name__)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(helloworld_route)
    return app
