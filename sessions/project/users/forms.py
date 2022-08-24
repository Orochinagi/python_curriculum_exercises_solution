from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,validators

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password',[validators.InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password',[validators.InputRequired()])