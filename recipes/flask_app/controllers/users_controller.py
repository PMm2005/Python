from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users_model import User

#-----------render route / desiplay login reg form ---------
@app.route('/')
def index():
    return render_template('index.html')


#----------- action route / register user ---------------

@app.route("/recipes", methods = ["POST"])
def register_user():
    #1 validate the inputs
    if User.validate_user(request.form) == False:
        return redirect ("/")
    #2 encrypt pswrd 
    hashed_password = User.encrypt_string(request.form["password"])
    #3 hashed pswrd --> db 

    data = {
        **request.form,
        "password": hashed_password
    }

    #enter the user in database
    user_id = User.create_one( data )
    
    session["user_id"] = user_id
    session["first_name"] = request.form["first_name"]

    return redirect("/recipes")


#---------Render Route / desiplay recipes----------


#---------------action route / Login user ------------


@app.route ("/recipes")
def login_user():
    current_user = User.get_one(request.form)
    if current_user  == None:
        flash("Email must already exist in the database", "error_login_email")
        return redirect ("/")
    if User.validate_password(request.form["password", current_user.pswrd]) == False:
        return redirect("/")
    session["user_id"] = current_user.id
    session["first_name"] = current_user.first_name

    return redirect ("/recipes")