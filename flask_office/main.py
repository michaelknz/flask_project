from flask import Flask,render_template
from text_editor import Text_Editor
from login import Login

app = Flask(__name__)
app.config.from_object('config')
text_editor=Text_Editor()
login=Login()

app.add_url_rule('/text_editor',view_func=text_editor.RenderEdPage)
app.add_url_rule('/text',view_func=text_editor.SendData)
app.add_url_rule('/login',view_func=login.RenderLogPage)

@app.route('/main_page')
def main_page():
    return render_template('mp/mp.html',title='mane_page')

if __name__ == '__main__':
    app.run()