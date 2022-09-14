from contextlib import redirect_stderr
from flask import Blueprint, render_template, request, url_for, redirect
from project.models import Owner
from project.owners.forms import formCreateOwner
from project import db

owners_blueprint = Blueprint(
    'owners',
    __name__,
    template_folder='templates')

@owners_blueprint.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        owner = Owner(first_name=request.form['first_name'],last_name = request.form['last_name'])
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('owners.index'))
    return render_template('index.html',owners = Owner.query.all())

@owners_blueprint.route('/new/')
def create():
    form = formCreateOwner()
    return render_template('create.html',form=form)