import db
from flask import Flask, redirect, url_for, request, render_template, request

app = Flask(__name__)

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/snacks/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        db.create_snack(request.form['name'],request.form['kind'])
        return redirect(url_for('index'))
    else:
        return render_template('index.html', snacks=db.get_all_snacks())

@app.route('/snacks/create/')
def create():
    return render_template('create.html')

@app.route('/snacks/<int:id>/', methods=['GET', 'PATCH','DELETE','POST'])
def show(id):
    if request.args.get('method')=='PATCH':
        db.update_snack_by_id(name=request.form['name'],kind=request.form['kind'],id=id)
        return redirect(url_for('index'))
    elif request.args.get('method')=='DELETE':
        db.delete_snack_by_id(id)
        return redirect(url_for('index'))
    else:
        return render_template('show.html',snack=db.show_snack_by_id(id))

@app.route('/snacks/<int:id>/edit/')
def edit(id):
    return render_template('edit.html',id=id)

if __name__=='__main__':
    db.create_table()
    app.run(debug=True)