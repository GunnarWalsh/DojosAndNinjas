from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import dojo

# Create
@app.route("/dojos/add_to_db", methods=["POST"])
def add_dojo_to_db():
    data = {
        "name": request.form["name"]
    }
    dojo.Dojo.create_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def individual_dojo(id):
    data = {
        "id" : id
    }
    return render_template("dojo.html", this_dojo = dojo.Dojo.get_one_dojo_with_ninjas(data))
# Read 
@app.route("/dojos")
def home():
    return render_template("dojos.html" , all_dojos = dojo.Dojo.return_dojos())




# Update 

# Delete
