from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home():
    return render_template("Form.html")

@app.route("/result", methods=["POST"])
def submittedinfo():
    username = request.form["username"]
    location_select = request.form["location_select"]
    FavLanguage_select = request.form["FavLanguage_select"]
    comment = request.form["comment"]

    return render_template("Display.html", username = username, location_select=location_select, FavLanguage_select=FavLanguage_select, comment=comment)


if __name__=="__main__":
    app.run(debug=True)

