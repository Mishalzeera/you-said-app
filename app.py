import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", number_list=[1, 2, 3])


@app.route("/partner_one")
def partner_one():
    partner_data = []
    with open("data/partner_one.json", "r") as partner_one_data:
        partner_data = json.load(partner_one_data)

    task_data_array = []
    with open("data/partner_one_tasks.json", "r") as tasks_data:
        task_data_array = json.load(tasks_data)
    return render_template("partner_one.html", partner=partner_data, tasks=task_data_array)


@app.route("/partner_two")
def partner_two():
    data = []
    with open("data/partner_two.json", "r") as more_json_data:
        data = json.load(more_json_data)

    tasks_data = []
    with open("data/partner_two_tasks.json", "r") as even_more_json_data:
        tasks_data = json.load(even_more_json_data)
    return render_template("partner_two.html", partner=data, tasks=tasks_data)


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
