from snack import Snacks
from flask import Flask, redirect, url_for, request, render_template, request
snack_list = [Snacks(name='perk',kind='chocolate'),Snacks(name='wavy',kind='chips'),Snacks(name='lays',kind='chips')]

app = Flask(__name__)

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/snacks/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        snack_list.append(Snacks(name=request.form['name'],kind=request.form['kind']))
        return redirect(url_for('index'))
    else:
        return render_template('index.html', snacks=snack_list)

@app.route('/snacks/create/')
def create():
    return render_template('create.html')

@app.route('/snacks/<int:id>/', methods=['GET', 'PATCH','DELETE','POST'])
def show(id):
    if request.args.get('method')=='PATCH':
        snack_list[id].name=request.form['name']
        snack_list[id].kind=request.form['kind']
        return redirect(url_for('index'))
    elif request.method=='POST':
        snack_list.pop(id)
        return redirect(url_for('index'))
    else:
        print(request.args.get('method'))
        return render_template('show.html',snack=snack_list[id])

@app.route('/snacks/<int:id>/edit/')
def edit(id):
    return render_template('edit.html',id=id)

if __name__=='__main__':
    app.run(debug=True)