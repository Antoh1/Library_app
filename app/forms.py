
#Import Form elements
from flask_wtf import Form
#import form field variable types
from wtforms import StringField, PasswordField, BooleanField, TextField, SubmitField, IntegerField, ValidationError
# Import Form validators
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from .models import User

# Define the signup form (WTForms)
class SignupForm(Form):
    """This class instanciate signup form
    instance to be rendered to SignUp html template"""

    name = StringField('Name', validators=[DataRequired(),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, numbers, dots or underscores')])
    email    = TextField('Email Address',
        validators=[Email(message='Put the right mail address'), DataRequired(message='Forgot your email address?'), Length(1, 64)])
    id_no = StringField('ID Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('SignUp')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_id_no(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('ID Number already registered.')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use.')


class LoginForm(Form):
    """This class instanciate login form
    instance to be rendered to login html template"""

    email = TextField('Email Address', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddBook(Form):
    """This class instanciate add_Book form
    instance to be rendered to admin_dashboard html template"""

    book_name = TextField('Book Name', validators=[DataRequired()])
    book_desc = TextField('Book Description', validators=[DataRequired()])
    book_category = TextField('Book Category', validators=[DataRequired()])
    submit = SubmitField('Add')
