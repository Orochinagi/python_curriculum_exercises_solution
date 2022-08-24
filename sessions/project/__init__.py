from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"

db = SQLAlchemy(app)

from project.users.views import users_blueprint

app.register_blueprint(users_blueprint,url_prefix='/users')

@app.route('/')
def root():
    return 'welcome to root directory'