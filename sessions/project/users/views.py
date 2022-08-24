from hashlib import new
from flask import Flask, redirect, render_template, url_for, Blueprint, request, session
from project import app, db
from project.users.forms import SignupForm, LoginForm
from project.models import Users
from project.models import bcrypt
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        newUser = Users(username=request.form['username'], password=request.form['password'])
        db.session.add(newUser)
        db.session.commit()
        return  redirect(url_for('users.login'))
    else:
        form = SignupForm(request.form)
        return render_template('signup.html',form = form)

@users_blueprint.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method=='POST':
        current_user = Users.query.filter_by(username=request.form['username']).first()
        if current_user and form.validate():
            if bcrypt.check_password_hash(current_user.password,request.form['password']):
                session['user_id'] = current_user.id
                return redirect(url_for('users.welcome'))
    else:        
        return render_template('login.html',form=form)

@users_blueprint.route('/welcome')
def welcome():
    if not session.get('user_id'):
        return 'You are not authorized'
    else:
        return 'This is the Welcome page'