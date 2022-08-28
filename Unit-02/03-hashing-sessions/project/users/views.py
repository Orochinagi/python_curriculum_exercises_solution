from project import app, db
from project.models import Users
from flask import redirect, render_template, url_for, Blueprint, request, flash, session
from project.users.form import SignupForm, LoginForm
from project import bcrypt
users_bp = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_bp.route('/signup/', methods=['GET','POST'])
def signup():
    form = SignupForm(request.form)
    if request.method=='POST' and form.validate():
        if Users.query.filter_by(username=request.form['username']).first():
            flash('Username already exists')
            return redirect(url_for('users.signup'))
        else:
            user = Users(request.form['username'],request.form['password'])
            db.session.add(user)
            db.session.commit()
            flash('User Created, Please Login')
        return redirect(url_for('users.login'))
    else:
        return render_template('signup.html',form=form)

@users_bp.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Users.query.filter_by(username=request.form['username']).first()
        if user:
            if bcrypt.check_password_hash(user.password,request.form['password']):
                session['user_id'] = user.id
                return redirect(url_for('users.welcome'))
            else:
                flash('Password is incorrect')
                return redirect(url_for('users.login'))
        else:
            flash('Username Doesnot exist')
            return redirect(url_for('users.login'))
    else:
        return render_template('login.html', form=form)
    
@users_bp.route('/welcome/', methods=['GET','POST'])
def welcome():
    if request.method == 'POST':
        session.pop('user_id')
        flash('You have successfully loged out')
        return redirect(url_for('users.login'))
    else:
        if not session.get('user_id'):
            flash('Please login to view the contents of this page')
            return redirect(url_for('users.login'))
        else:
            flash('You have succesfully loged in')
            return render_template('welcome.html')