from project import db, app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)