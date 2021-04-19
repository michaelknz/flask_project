from flask import Flask
from forms import LoginForm
from flask import render_template,request,flash,redirect,url_for
from models import User
from models import db

class Login:
    def __init__(self):
        pass
    def RenderLogPage(self):
        form = LoginForm()
        if request.method=='POST':
            if(db.session.query(User.id).filter_by(nickname=request.form['login']).first() is not None):
                return redirect(url_for('existing_login'))
            elif(db.session.query(User.id).filter_by(email=request.form['email']).first() is not None):
                return redirect(url_for('existing_email'))
            else:
                user=User(request.form['login'],request.form['password'],request.form['email'])
                db.session.add(user)
                db.session.commit()
        return render_template('login/login.html', title='Sign In', form=form)