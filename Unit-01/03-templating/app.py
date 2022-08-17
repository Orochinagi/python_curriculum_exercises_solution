from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)
#part1

@app.route('/person/<name>/<age>/')
def person(name,age):
    return render_template('person.html',name=name,age=age)

#part2

@app.route('/add/<int:num1>/<int:num2>/')
def add(num1,num2):
    return 'The sum of {} + {} is {}'.format(num1,num2,num1+num2)

@app.route('/sub/<int:num1>/<int:num2>/')
def sub(num1,num2):
    return 'The difference of {} - {} is {}'.format(num1,num2,num1-num2)

@app.route('/mul/<int:num1>/<int:num2>/')
def mul(num1,num2):
    return 'The product of {} * {} is {}'.format(num1,num2,num1*num2)

@app.route('/div/<int:num1>/<int:num2>/')
def div(num1,num2):
    return 'The quotient of {} / {} is {}'.format(num1,num2,num1/num2)

@app.route('/math/', methods=['POST','GET'])
def maths():
    if request.method=='POST':
        return redirect(url_for(request.form['calculation'],num1=request.form['num1'],num2=request.form['num2']))
    else:
        return redirect(url_for('calculate'))
        
@app.route('/calculate',methods=['POST','GET'])
def calculate():
    return render_template('calc.html')

if __name__=='__main__':
    app.run(debug=True)