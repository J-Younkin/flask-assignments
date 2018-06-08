from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/result',methods=['POST'])
def result():
    return render_template("index2.html")

@app.route('/danger',methods=['GET'])
def danger():
    print("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')

app.run(debug=True) 



