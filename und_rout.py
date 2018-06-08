from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/flask')
def show_user_profile():
    return "Hi Flask"

@app.route('/repeat/35/hello')
def repeat_hello():
    i = 1
    repeat = ""
    while i < 36:
        repeat += "hello "
        i+=1
    return repeat

@app.route('/repeat/99/dogs')
def repeat_dogs():
    i = 1
    repeat = ""
    while i < 100:
        repeat += "dogs "
        i+=1
    return repeat




app.run(debug=True)