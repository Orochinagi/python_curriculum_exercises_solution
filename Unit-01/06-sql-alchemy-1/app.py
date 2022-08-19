from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-sql-snacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snacks(db.Model):
    __tablename__ = 'snacks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    def __init__(self,name,kind):
        self.name = name
        self.kind = kind

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/snacks/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        db.session.add(Snacks(request.form['name'],request.form['kind']))
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('index.html', snacks=Snacks.query.all())

@app.route('/snacks/create/')
def create():
    return render_template('create.html')

@app.route('/snacks/<int:id>/', methods=['GET', 'PATCH','DELETE','POST'])
def show(id):
    if request.args.get('method')=='PATCH':
        snack = Snacks.query.get(id)
        snack.name = request.form['name']
        snack.kind = request.form['kind']
        db.session.add(snack)
        db.session.commit()
        return redirect(url_for('index'))
    elif request.args.get('method')=='DELETE':
        snack = Snacks.query.get(id)
        db.session.delete(snack)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('show.html',snack=Snacks.query.get(id))

@app.route('/snacks/<int:id>/edit/')
def edit(id):
    return render_template('edit.html',id=id)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)