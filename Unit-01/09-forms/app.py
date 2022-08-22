from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators, TextAreaField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-sql-snacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'any string works here'
db = SQLAlchemy(app)

class formCreateUser(FlaskForm):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name',[validators.InputRequired()])

class formCreateMessage(FlaskForm):
    content = TextAreaField('Content', [validators.InputRequired()])

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

class Messages(db.Model):
    __tablename__='Messages'
    uid = db.Column(db.Integer, foreign_key="Users.id")
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __init__(self,uid,content):
        self.uid=uid
        self.content=content
    
@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/users/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        user = Users(first_name=request.form['first_name'], last_name=request.form['last_name'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        users=Users.query.all()
        return render_template('index.html',users=users)

@app.route('/users/<int:id>/edit/', methods=['GET','POST'])
def edit(id):
    if request.args.get('method')=='PATCH':
        user = Users.query.get(id)
        user.first_name = request.form['fname']
        user.last_name = request.form['lname']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    elif request.args.get('method') == 'DELETE':
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit.html')

@app.route('/users/new/')
def create():
    form = formCreateUser(request.form)
    return render_template('create.html',form=form)

@app.route('/messages/')
def mindex():
    messages = Messages.query.all()
    return render_template('mindex.html',messages=messages)

@app.route('/users/<int:uid>/messages/', methods=['POST','GET'])
def show_user_messages(uid):
    if request.method=='POST':
        message = Messages(uid=uid, content=request.form['content'])
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('show_user_messages',uid=uid))
    else:
        messages = Messages.query.filter_by(uid=uid)
        return render_template('userMessages.html', messages=messages)

@app.route('/users/<int:uid>/messages/new/')
def create_message_for_user(uid):
    form = formCreateMessage(request.form)
    return render_template('createUserMessage.html',uid=uid,form=form)

@app.route('/users/<int:uid>/messages/<int:mid>/edit/',methods=['POST','GET'])
def message_edit(uid,mid):
    if request.args.get('method')=='PATCH':
        message = Messages.query.get(mid)
        message.content=request.form['content']
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('show_user_messages',uid=uid))
    elif request.args.get('method')=='DELETE':
        message = Messages.query.get(mid)
        db.session.delete(message)
        db.session.commit()
        return redirect(url_for('show_user_messages',uid=uid))
    else:
        return render_template('editUserMessage.html',uid=uid,mid=mid)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)