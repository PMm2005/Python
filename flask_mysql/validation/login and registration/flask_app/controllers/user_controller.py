from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User



#display lgin/reg form
@app.route('/')
def index():
    return render_template('index.html')

# action route registe a user

@app.route("/user/register", methods=["POST"])
def register_user():
    if User.validate_user(request.form) == False:
        return redirect("/")

    hashed_password = User.encrypt_string(request.form["password"])
    data = {
        **request.form,
        "password": hashed_password
    }

    #store user in database
    user_id = User.create_one(data)
    session["user_id"] = user_id
    session ["first_name"] = request.form["first_name"]
    session ["last_name"] = request.form["last_name"]
    return redirect("/recipes")

#action route login user


@app.route("/user/login", methods = ["POST"])
def login_user():
    current_user = User.get_one(request.form)
    if current_user == None:
        flash("This email does not exist ", "error_login_email")
        return redirect("/")
    if User.validate_password(request.form["password"], current_user.password) == False:
        return redirect("/")
    session["user_id"] = current_user.id
    session["first_name"] = current_user.first_name

    return redirect("/recipes")