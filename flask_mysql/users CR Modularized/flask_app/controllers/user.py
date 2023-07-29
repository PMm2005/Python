from flask import Flask, render_template, session, request, redirect
from flask_app.models.user import users


app = Flask(__name__)
app.secret_key = "123123a"



@app.route('/users')
def userstable():
    all_users = users.get_all()
    print(all_users)
    return render_template("/users.html", all_users = all_users)

@app.route("/user/new")
def display_form():
    return render_template("/form.html")


@app.route("/processForm", methods = ['POST'])
def create_user():
    print(request.form)
    users.create(request.form)
    return redirect("/users")

