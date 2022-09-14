from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flask-blueprints.db'
app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"

db = SQLAlchemy(app)
from project.owners.views import owners_blueprint
app.register_blueprint(owners_blueprint,url_prefix='/owners')
db.create_all()
@app.route('/')
def root():
    return "HELLO BLUEPRINTS!"