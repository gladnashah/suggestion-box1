from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config[config])
	config[config].init_app(app)

	db = SQLAlchemy(app)
	db.init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	toolbar = DebugToolbarExtension(app)

	

	from app import  models
	from . import views

	return app

	