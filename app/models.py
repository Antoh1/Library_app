# Import the database object (db) from the main application module
from app import db

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from . import loginManager

# Define a User model class as one of the database tables

class User(UserMixin, db.Model):


    id = db.Column(db.Integer, primary_key=True)

    # User Name
    name = db.Column(db.String,  nullable=False)

    # Identification Data: email , id_no and password 
    email    = db.Column(db.String,  index=True,
                                            unique=True)
    id_no    = db.Column(db.Integer,  nullable=False,
                                            unique=True)
    password_hash = db.Column(db.String,  nullable=False)

    def __init__(self, name, email, id_no, password):
        self.name = name
        self.email = email
        self.id_no = id_no
        self.password = password

    @property   
    def password(self):        
        raise AttributeError('password is not a readable attribute')
        
    @password.setter    
    def password(self, password):   
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password) 

    @loginManager.user_loader 
    def load_user(user_id):    
        return User.query.get(int(user_id))     



    def __repr__(self):
        return '<User %r>' % (self.nickname)                 