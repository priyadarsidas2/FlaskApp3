import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

############################
#DATABASE SETUP#############
############################

app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#############################
#LOGIN CONFIGS###############
#############################

login_manager.init_app(app)
login_manager.login_view = 'users.login'

#############################
#### BLUEPRINT CONFIGS ######
#############################

# Import these at the top if you want
# We've imported them here for easy reference
from resumeapp.core.views import core
from resumeapp.resume.views import resume
from resumeapp.error_pages.handlers import error_pages
from resumeapp.users.views import users

# Register the apps
app.register_blueprint(resume)
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
