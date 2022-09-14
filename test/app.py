from flask import Flask, redirect, request, url_for, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators, TextAreaField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super secret string'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class authData(db.Model):
    __tablename__ = 'Auth_Data'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self,username,password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

class formAuthData(FlaskForm):
    username = StringField('Username',[validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])

@app.route('/signup/', methods=['GET','POST'])
def signup():
    form = formAuthData(request.form)
    if request.method=='POST':
        user = authData(username=request.form['username'],password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html',form=form)

@app.route('/login/',methods=['GET','POST'])
def login():
    form = formAuthData(request.form)
    if request.method=='POST':
        user = authData.query.filter_by(username=request.form['username'])[0]
        if bcrypt.check_password_hash(user.password,request.form['password']):
                    return redirect(url_for('welcome'))
    else:
        return render_template('login.html',form=form)

@app.route('/welcome/')
def welcome():
    return 'Welcome to my app'

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)