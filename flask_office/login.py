from flask import Flask
from forms import LoginForm
from flask import render_template

class Login:
    def __init__(self):
        pass
    def RenderLogPage(self):
        form = LoginForm()
        return render_template('login/login.html', title='Sign In', form=form)