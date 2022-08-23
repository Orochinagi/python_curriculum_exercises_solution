from project import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CreateUserForm(FlaskForm):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])