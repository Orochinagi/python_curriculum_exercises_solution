from flask import Flask

app = Flask(__name__)

@app.route('/welcome/')
def welcome():
    return 'Welcome'

@app.route('/welcome/home/')
def welcomeHome():
    return 'Welcome Home'

@app.route('/welcome/back/')
def welcomeBack():
    return 'Welcome Back'

@app.route('/sum/')
def sum():
    sum = 5+5
    return 'The sum is %d'%sum

if __name__=='__main__':
    app.run(debug=True)