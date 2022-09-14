from project import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class formCreateOwner(FlaskForm):
    first_name = StringField('first_name',[validators.InputRequired()])
    last_name = StringField('last_name',[validators.InputRequired()])