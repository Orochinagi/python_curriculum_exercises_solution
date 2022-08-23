from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flask-blueprints.db'
app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"

db = SQLAlchemy(app)
from project.users.view import user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users/')

@app.route('/')
def root():
    return 'Welcome to root'