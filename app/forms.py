
#Import Form elements
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, TextField, SubmitField
# Import Form validators
from wtforms.validators import DataRequired, Email, Length 

# Define the signup form (WTForms)
class signupForm(Form):    	
	name = StringField('Last Name', validators=[DataRequired()])
	email    = TextField('Email Address', [Email(message='Put the right mail address'), DataRequired(message='Forgot your email address?')])
	id_no = StringField('ID Number', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(message="Must provide password")])
	submit = SubmitField('SignUp')

class loginForm(Form):
    email = TextField('Email Address', [Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])