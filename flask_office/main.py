from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import User,db
from text_editor import Text_Editor
from login import Login

app = Flask(__name__)
app.config.from_object('config')
app.debug=True
db.init_app(app)

text_editor=Text_Editor()
login=Login()


app.add_url_rule('/text_editor',view_func=text_editor.RenderEdPage)
app.add_url_rule('/text',view_func=text_editor.SendData)
app.add_url_rule('/login',view_func=login.RenderLogPage,methods = ['GET', 'POST'])

@app.route('/main_page')
def main_page():
    return render_template('mp/mp.html',title='mane_page')

if __name__ == '__main__':
    app.run()