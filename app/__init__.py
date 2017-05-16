# Import flask and template operators
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import basedir
from flask_migrate import Migrate, MigrateCommand
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

loginManager = LoginManager()
loginManager.session_protection = 'strong'
loginManager.init_app(app)
loginManager.login_view = 'login'
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app import views, models
    
