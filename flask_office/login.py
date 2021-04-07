from flask import Flask
from forms import LoginForm
from flask import render_template,request,flash
from models import User
from models import db

class Login:
    def __init__(self):
        pass
    def RenderLogPage(self):
        form = LoginForm()
        if request.method=='POST':
            if(db.session.query(User.id).filter_by(nickname=request.form['login']).first() is None):
                user=User(request.form['login'],request.form['password'],request.form['email'])
                db.session.add(user)
                db.session.commit()
            else:
                pass
        return render_template('login/login.html', title='Sign In', form=form)