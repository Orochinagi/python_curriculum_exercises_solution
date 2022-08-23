from project import app, db
from flask import render_template, request, redirect, url_for, Blueprint
from project.models import Users
from project.users.forms import CreateUserForm

user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='templates'
)

@user_blueprint.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        user = Users(first_name=request.form['first_name'], last_name=request.form['last_name'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.index'))
    else:
        return render_template('index.html',users = Users.query.all())

@user_blueprint.route('/new/')
def create():
    form = CreateUserForm()
    return render_template('create.html',form=form)