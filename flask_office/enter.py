from flask import Flask
from forms import EnterForm
from flask import render_template,request,flash,redirect,url_for
from models import User
from models import db
import consts

class Enter:
    def __init__(self):
        pass
    def RenderEnterPage(self):
        form = EnterForm()
        if(request.method=='POST'):
            user=db.session.query(User.id).filter_by(nickname=request.form['login']).first()
            if(user is None):
                return redirect(url_for('login_does_not_exist'))
            if(request.form['password']!=User.query.get(user.id).password):
                return redirect(url_for('wrong_password'))
            else:
                user_tabel=User.query.get(user[0])
                consts.is_auth=True
                consts.user=user_tabel
                return redirect(url_for('main_page'))
        return render_template('enter/enter.html', title='Enter', is_auth=consts.is_auth, form=form)