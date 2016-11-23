# Import flask and template operators
import os
from flask import Flask, render_template
from flask_login import LoginManager
from config import basedir
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
loginManager = LoginManager()
loginManager.session_protection = 'strong'
loginManager.init_app(app)
loginManager.login_view = 'login'
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app import views, models

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
