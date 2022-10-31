from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from resumeapp import db
from resumeapp.models import User
from resumeapp.users.forms import RegistrationForm, LoginForm, UpdateUserForm

users = Blueprint('users', __name__)

#register
@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    
    return render_template('register.html', form=form)

#login
@users.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            
            login_user(user)
            flash('Log in Success!')
            
            next = request.args.get('next')
            
            if next== None or not next[0] == '/':
                next = url_for('resume.create_post')
                
            return redirect(next)
        
    return render_template('login.html', form=form)

#logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.login"))

#account
@users.route('/account', methods= ["GET", "POST"])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        return redirect(url_for('users.account'))
    
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    return render_template('account.html', form = form)