from flask import Flask,render_template

app = Flask(__name__)

@app.route('/main_page')
def main_page():
    return render_template('mp/mp.html')

app.run(debug = False)