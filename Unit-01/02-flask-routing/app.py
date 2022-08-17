from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

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
        return redirect(url_for(request.form['operation'],num1=request.form['num1'],num2=request.form['num2']))
    else:
        return render_template('math.html')

if __name__=='__main__':
    app.run(debug=True)