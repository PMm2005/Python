from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def gotodojo():
    return redirect('/dojos')

@app.route('/dojos')
def new_dojos():
    dojos= Dojo.get_all()
    return render_template('dojos.html',dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def one_dojo(dojo_id):
    data = {
        'id':dojo_id,
        'dojo_id':dojo_id
    }
    dojo = Dojo.get_one(data)
    ninjas = Ninja.get_specefic(data)
    return render_template('read.html',dojo=dojo,ninjas=ninjas)