# Import the database object (db) from the main application module
from app import db
#import security module for encrypting passwords in the database
from werkzeug.security import generate_password_hash, check_password_hash
#import UserMixin module for validating user login states
from flask_login import UserMixin
#login manager to validate user login
from . import loginManager

# Define a User model class as one of the database tables

class User(db.Model, UserMixin):
    """This class creates users database table instance
     and sets table field names"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # User Name
    name = db.Column(db.String,  nullable=False)

    # Identification Data: email , id_no and password
    email    = db.Column(db.String,  index=True, unique=True)

    id_no    = db.Column(db.Integer, nullable=False, unique=True)

    password_hash = db.Column(db.String, nullable=True)

    def __init__(self, name, email, id_no, password):
        self.name = name
        self.email = email
        self.id_no = id_no
        self.password_set(password)

    #property checking for hashable password input
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    def password_set(self, password):
        #method to encrypt password stored in database
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        #method to compare encrypted password in database and post request
        return check_password_hash(self.password_hash, password)

    @loginManager.user_loader
    def load_user(user_id):
        #method to validate user login
        return User.query.get(int(user_id))



    def __repr__(self):
        return '<User %r>' % (self.name)

class AvailableBooks(db.Model):
    """This class creates available_books database table instance
     and sets table field names"""

    __tablename__ = 'available_books'

    id = db.Column(db.Integer, primary_key=True)

    book_name = db.Column(db.String, nullable=False)

    book_desc = db.Column(db.Text, nullable=False)

    book_category = db.Column(db.Text, nullable=False)



    def __init__(self, bookName, bookDescription, bookCategory):

        self.book_name = bookName
        self.book_desc = bookDescription
        self.book_category = bookCategory

    def __repr__(self):
        return '<Book %r>' % (self.book_name)


class BorrowedBooks(db.Model):
    """This class creates borrowed_books database table instance
     and sets table field names"""

    __tablename__ = 'borrowed_books'

    id = db.Column(db.Integer, primary_key=True)

    book_borrower = db.Column(db.String, nullable=False)

    book_name = db.Column(db.String, nullable=False, index=True)

    borrow_date = db.Column(db.Date, nullable=False, index=True)

    borrow_days = db.Column(db.String, nullable=False)

    delay_charge = db.Column(db.String, nullable=True)

    def __init__(self, borrower, bookName, borrowDate, borrowDays, delayCharge):

        self.book_borrower = borrower
        self.book_name = bookName
        self.borrow_date = borrowDate
        self.borrow_days = borrowDays
        self.delay_charge = delayCharge

    def __repr__(self):
        return '<Book %r>' % (self.book_name)

class TotalBooks(db.Model):
    """This class creates total books database instance table object"""

    __tablename__ = 'total_books'

    id = db.Column(db.Integer, primary_key=True)

    book_name = db.Column(db.String, nullable=False, index=True)

    book_quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, bookName, bookQuantity):

        self.book_name = bookName
        self.book_quantity = bookQuantity

    def __repr__(self):
        return '<Book %r>' % (self.book_name)
