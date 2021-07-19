from flask import Flask

#data base object 
from .models import db

#blueprints
from .controllers.admin import admin_route


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1bansal99@localhost:3306/passionpro'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(admin_route)
    return app
