from crypt import methods
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import ninja, dojo

@app.route("/ninjas")
def ninja_input():
    return render_template("ninjas.html" , all_dojos = dojo.Dojo.return_dojos())

@app.route("/ninjas/add_to_db" , methods=["POST"])
def add_ninja_to_db():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    ninja.Ninja.create_ninja(data)
    return redirect("/dojos")


