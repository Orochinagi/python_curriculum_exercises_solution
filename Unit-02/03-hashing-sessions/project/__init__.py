from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACCT_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"

db = SQLAlchemy(app)

from project.users.views import users_bp
app.register_blueprint(users_bp)

@app.route('/')
def root():
    return 'This is the Root Path'