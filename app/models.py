# Import the database object (db) from the main application module
from app import db

# Define a User model class as one of the database tables

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
     # User Name
    name = db.Column(db.String,  nullable=False)

    # Identification Data: email , id_no and password 
    email    = db.Column(db.String,  index=True,
                                            unique=True)
    id_no    = db.Column(db.Integer,  nullable=False,
                                            unique=True)
    password = db.Column(db.String,  nullable=False)

    def __init__(self, name, email, id_no, password):
        self.name = name
        self.email = email
        self.id_no = id_no
        self.password = password



    def __repr__(self):
        return '<User %r>' % (self.nickname)                 