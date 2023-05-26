from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def home():
    visit_count = session.get('visit_count', 0)
    visit_count += 1
    session['visit_count'] = visit_count
    return render_template('index.html', visit_count=visit_count)

@app.route('/destroy_session')
def destroysession():
    session.clear()
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)  

