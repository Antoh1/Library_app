
#import dependencies
from flask import render_template, flash, redirect, session, url_for, request, g
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from app import app, db
# Import module forms
from forms import SignupForm, LoginForm, AddBook

from flask_login import login_user, logout_user, login_required 

# Import module models 
from models import User, AvailableBooks


# Set the route and accepted methods
@app.route('/')
@app.route('/Home')
def Home():
    """This method renders the landing page upon GET reques by user"""

    return render_template('Home.html', title='Home')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """This function renders signup form to signup html template 
    and handles the POST request from the form"""

	# If sign in form is submitted
    form = SignupForm(request.form)

    # Verify the signup in form
    if form.validate_on_submit():
        user = User(name= form.name.data, email=form.email.data, 
            id_no=form.id_no.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a Library valid User')
        return redirect(url_for('user_login'))
    flash('Enter unique Name, Email and ID Number')    
    return render_template('signup.html', form=form)


# decorator to register route for user login controller
@app.route('/user_login', methods=['GET','POST'])
def user_login():
    """This function renders login form to login html template 
    and handles the POST request from the form"""

    error = None
    user_form = LoginForm(request.form)
    if user_form.validate_on_submit():
        user = User.query.filter_by(email=user_form.email.data).first()
        if user is not None and user.verify_password(user_form.password.data):
            login_user(user)
            session['logged_in']=True
            flash('You are logged in as Library User')
            return redirect(url_for('.viewBooks'))
        flash('Invalid username or password.')    
        return render_template('user_login.html', form=user_form, error=error)
    flash('Enter a valid email address')    
    return render_template('user_login.html', form=user_form, error=error) 

#decorator to register route for admin login controller
@app.route('/admin_login', methods=['GET','POST'])
def admin_login():
    """This function renders administrator login form to admin login html template 
    and handles the POST request from the form"""

    error = None
    admin_form = LoginForm(request.form)
    if request.method == 'POST':
        if admin_form.validate_on_submit():
            if request.form['email'] != 'admin@gmail.com' or request.form['password'] != 'admin':
                error = 'Invalid login credentials, Try again'
            else:
                session['logged_in']=True
                flash('You are logged in as Library Admin')
                return redirect(url_for('add_Book'))
        else:
            flash('Enter valid Admin email address and password combination')
            render_template('admin_login.html', form=admin_form, error=error)
    return render_template('admin_login.html', form=admin_form, error=error)

@app.route('/logout')
@login_required 
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('Home')) 

@app.route('/admin_dashboard', methods=['GET','POST'])
def add_Book():
    """This function renders addBook form to admin_dashboard html template 
    and updates the POST request from the form to the database table"""

    form = AddBook(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            bookAdd = AvailableBooks(form.book_name.data, form.book_desc.data, form.book_category.data)
            db.session.add(bookAdd)
            db.session.commit()
            flash('Book Successfully added... Add Another Book')
            return render_template('admin_dashboard.html', form=form)
        flash('Fill all the Fields')
        return render_template('admin_dashboard.html', form=form)
    return render_template('admin_dashboard.html', form=form)

@app.route('/user_dashboard', methods=['GET','POST'])            
def viewBooks():
    """This function renders books database object to user_dashboard html template 
    and list all the books available in the Library"""

    if request.method=='GET':
        books = AvailableBooks.query.all()
        return render_template('user_dashboard.html', books=books)



