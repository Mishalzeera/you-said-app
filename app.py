import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/partner_one")
def partner_one():
    return render_template("partner_one.html")


@app.route("/partner_two")
def partner_two():
    return render_template("partner_two.html")


@app.route("/login_register")
def login_register():
    return render_template("login_register.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5500")),
        debug=True
    )
