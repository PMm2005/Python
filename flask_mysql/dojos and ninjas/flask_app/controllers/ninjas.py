from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo



@app.route('/ninjas')
def index():
    
    dojos=Dojo.get_all()
    return render_template("add_ninja.html",dojos = dojos)


@app.route('/ninjas/new', methods=['POST'])
def new_ninja():
    Ninja.create(request.form)
    return redirect('/dojos/'+str(request.form['dojo_id']))
