from flask import Flask
from forms import LoginForm
from flask import render_template,request,flash,redirect,url_for
from models import User
from models import db
import consts

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
            elif(request.form['password']!=request.form['cpassword']):
                return redirect(url_for('different_passwords'))
            else:
                user=User(request.form['login'],request.form['password'],request.form['email'])
                db.session.add(user)
                db.session.commit()
                consts.is_auth=True
                return redirect(url_for('main_page'))
        return render_template('login/login.html', title='Sign In', is_auth=consts.is_auth, form=form)