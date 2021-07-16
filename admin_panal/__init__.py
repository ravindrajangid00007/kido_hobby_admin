from flask import Flask

#data base object 
from .models import db

#blueprints
from .controllers.admin import admin_route


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:ravindra@database-1.cnnmnb9m4bjr.ap-south-1.rds.amazonaws.com/KIDO_ADMIN_DATABASE'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(admin_route)
    return app
