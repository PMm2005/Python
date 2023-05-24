from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index2():
    return render_template("index2.html")

@app.route('/play/<string:x>')
def boxes(x):
    count = int(x)
    return render_template("index.html", count=count)

@app.route('/play/<string:x>/<string:color>')
def index3(x,color):
    count = int(x)
    return render_template("index3.html", count=count, color=color)


if __name__=="__main__":
    app.run(debug=True)  

