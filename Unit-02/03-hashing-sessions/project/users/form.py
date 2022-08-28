from ast import Pass
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class SignupForm(FlaskForm):
    username = StringField('Username: ', [validators.InputRequired()])
    password = PasswordField('Password: ', [validators.InputRequired(), validators.length(min=6)])

class LoginForm(FlaskForm):
    username = StringField('Username: ', [validators.InputRequired()])
    password = PasswordField('Password: ', [validators.InputRequired(), validators.length(min=6)])
