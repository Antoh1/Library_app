
#import dependencies
from flask import render_template, flash, redirect, session, url_for, request, g
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash
# Import the database object from the main app module
from app import app, db
# Import module forms
from forms import signupForm, loginForm, addBook

from flask_login import login_user 

from flask_login import login_required
# Import module models 
from models import User, availableBooks

# Set the route and accepted methods
@app.route('/')
@app.route('/Home')
def Home():
    return render_template('Home.html', title='Home')
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
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)
# decorator to register route for user login controller
@app.route('/login', methods=['GET','POST'])
def user_login():
    error = None
    user_form = loginForm(request.form)
    if request.method == 'POST':
        if user_form.validate_on_submit():
            user = User.query.filter_by(email=user_form.email.data).first()
            if user is not None and user.verify_password(user_form.password.data):
                login_user(user)
                session['logged_in']=True
                flash('You are logged in')
                return redirect(url_for('.user_dashboard'))
            flash('Invalid username or password.')    
        return render_template('login.html', form=user_form, error=error)
    return render_template('login.html', form=user_form, error=error) 

#decorator to register route for admin login controller
@app.route('/admin_login', methods=['GET','POST'])
@login_required
def admin_login():
    error = None
    admin_form = loginForm(request.form)
    if request.method == 'POST':
        if admin_form.validate_on_submit():
            if request.form['email'] != 'admin@gmail.com' or request.form['password'] != 'admin':
                error = 'Invalid login credentials, Try again'
            else:
                session['logged_in']=True
                flash('You are logged in')
                return render_template('admin_dashboard.html', form=admin_form)
        else:
            render_template('admin_login.html', form=admin_form, error=error)
    return render_template('admin_login.html', form=admin_form, error=error)

@app.route('/admin_dashboard', methods=['GET','POST'])
@login_required
def add_Book():
    form = addBook(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            bookAdd = availableBooks(form.book_name.data, form.book_desc.data, form.book_category.data)
            db.session.add(bookAdd)
            db.session.commit()
            flash('One Book added')
            return render_template('admin_dashboard.html', form=form)
        flash('Fill all the Fields')
        return render_template('admin_dashboard.html', form=form)
    return render_template('admin_dashboard.html', form=form)

@app.route('/user_dashboard', methods=['GET','POST'])            
def viewBooks():
    if request.method=='GET':
        books = availableBooks.query.all()
        flash('These are the books in the Library')
        return render_template('user_dashboard.html', books=books)



