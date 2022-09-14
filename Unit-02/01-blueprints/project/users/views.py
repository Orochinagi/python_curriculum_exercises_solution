from project import app, db
from project.models import Users
from flask import redirect, render_template, url_for, Blueprint, request, flash
from project.users.form import CreateUserForm

users_bp = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_bp.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        if request.args.get('method') == 'PATCH':
            user = Users.query.get(request.args.get('id'))
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            db.session.add(user)
            db.session.commit()
            flash('Updated User Info Successfully')
            return redirect(url_for('users.index'))
        elif request.args.get('method') == 'DELETE':
            user = Users.query.get(request.args.get('id'))
            db.session.delete(user)
            db.session.commit()
            flash('Deleted User Successfully')
            return redirect(url_for('users.index'))
        else:
            user = Users(first_name=request.form['first_name'],last_name=request.form['last_name'])
            db.session.add(user)
            db.session.commit()
            flash('Successfully Added User')
            return redirect(url_for('users.index'))
    else:
        return render_template('index.html',users=Users.query.all())

@users_bp.route('/new/')
def create():
    form = CreateUserForm()
    return render_template('create.html',form=form)

@users_bp.route('/<int:id>/edit/')
def edit(id):
    form = CreateUserForm()
    current_user = Users.query.get(id)
    return render_template('edit.html',id=id,form=form)