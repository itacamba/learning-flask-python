from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "H3LL0"
app.permanent_session_timeline = timedelta(minutes=1)
# timedelta(days=5)
# timedelta(minutes=10)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # the line below makes our session permanent / will last as long you declared it in line 6
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else: 
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return "<h1>Hey %s!</h1>" % user
    else:
        return redirect(url_for("login"))


@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))




if __name__ == "__main__":
    app.run(debug=True)