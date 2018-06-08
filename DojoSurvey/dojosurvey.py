from flask import Flask, render_template
app = Flask(name)

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/result',methods=['POST'])
def result():

    return render_template("index2.html")

@app.route('/danger')
def danger():
    print("a user tried to visit /danger. we have redirected the user to /")
    return render_template("index.html")

app.run(debug=True) 



