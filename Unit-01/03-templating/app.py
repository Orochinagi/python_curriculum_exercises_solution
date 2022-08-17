from flask import Flask, render_template,redirect, url_for, request
import requests, re
from bs4 import BeautifulSoup as bs

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

#part 3

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/results/')
def results():
    keyword = request.args.get('keyword')
    resp = requests.get(url='https://news.google.com')
    soup = bs(resp.content,'html.parser')
    headlines = soup.find_all(class_ = 'DY5T1d RZIKme',string = re.compile(keyword))
    return render_template('results.html',headlines=headlines)

if __name__=='__main__':
    app.run(debug=True)