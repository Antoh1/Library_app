
#import dependencies
from flask import render_template, flash, redirect, session, url_for, request, g
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from app import app, db
# Import module forms
from forms import signupForm
from forms import loginForm
# Import module models 
from models import User

# Set the route and accepted methods
@app.route('/signup', methods=['GET', 'POST'])
def signup():

	# If sign in form is submitted
    form = signupForm(request.form)

    # Verify the signup in form
    if request.method == 'POST' and form.validate():
        user = User(name= form.name.data, email=form.email.data, 
            id_no=form.id_no.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a Library valid User')
        return render_template('login.html', form=form)
    else:
        return render_template('signup.html', form=form)
# decorator to register route for user login controller
@app.route('/user_login', methods=['GET','POST'])
def user_login():
    error = None
    form = loginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            #if request.form['email'] != 'admin@gmail.com' or request.form['password'] != 'admin':
                #error = 'Invalid login credentials, Try again'
            else:
                session['logged_in']=True
                flash('You are logged in')
                return redirect(url_for('signup'))
        else:
            render_template('user_login.html', form=form, error=error)
    return render_template('user_login.html', form=form, error=error) 

#decorator to register route for admin login controller
@app.route('/admin_login', methods=['GET','POST'])
def admin_login():
     error = None
    form = loginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form['email'] != 'admin@gmail.com' or request.form['password'] != 'admin':
                error = 'Invalid login credentials, Try again'
            else:
                session['logged_in']=True
                flash('You are logged in')
                return redirect(url_for('admin_panel'))
        else:
            render_template('admin_login.html', form=form, error=error)
    return render_template('admin_login.html', form=form, error=error)                         