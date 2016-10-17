from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from app import config
db = SQLAlchemy()
mail = Mail()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config[config_name])
    config.config[config_name].init_app(app)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    mail.init_app(app)
    moment.init_app(app)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    db.init_app(app)
    # attach routes and custom error pages herereturn app
    return app


app = create_app('default')
