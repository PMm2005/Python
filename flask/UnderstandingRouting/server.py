from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/<Name>')
def greetingFunction( Name):
    return f"Hi : { Name}"

@app.route('/repeat/35/hello/<name>/<int:times>')
def greeting(name,times):
    return f"Hi { name}" * times

@app.route('/repeat/80/bye/<name>/<int:times>')
def goodbye(name,times):
    return f"Bye { name}" * times

if __name__=="__main__":
    app.run(debug=True)

