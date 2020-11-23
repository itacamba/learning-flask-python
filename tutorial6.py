from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "H3LL0"
app.permanent_session_timeline = timedelta(minutes=5)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        flash("Logged in Successfully!")
        return redirect(url_for("user"))
    else: 
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))


@app.route('/logout')
def logout():
        # flash(<message>, <category>)
    flash("you have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))




if __name__ == "__main__":
    app.run(debug=True)