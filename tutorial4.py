from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else: 
        return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return "<h1>Hey %s!</h1>" % usr

if __name__ == "__main__":
    app.run(debug=True)