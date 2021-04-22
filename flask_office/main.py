from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import User,db
from base_test import Base_Test
from login import Login
from enter import Enter
from error import Error
import consts

app = Flask(__name__)
app.config.from_object('config')
app.debug=True
db.init_app(app)

BaseTest=Base_Test()
login=Login()
enter=Enter()
error=Error()


app.add_url_rule('/base_test',view_func=BaseTest.RenderBaseTestPage)
app.add_url_rule('/text',view_func=BaseTest.SendData)
app.add_url_rule('/login',view_func=login.RenderLogPage,methods = ['GET', 'POST'])
app.add_url_rule('/enter',view_func=enter.RenderEnterPage,methods=['GET', 'POST'])
app.add_url_rule('/exist_login',view_func=error.existing_login)
app.add_url_rule('/exist_email',view_func=error.existing_email)
app.add_url_rule('/diff_pass',view_func=error.different_passwords)
app.add_url_rule('/login_does_not_exist',view_func=error.login_does_not_exist)
app.add_url_rule('/wrong_password',view_func=error.wrong_password)

@app.route('/main_page')
def main_page():
    return render_template('mp/mp.html',title='main_page',is_auth=consts.is_auth)

@app.route('/auth')
def auth():
    consts.is_auth=True
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run()