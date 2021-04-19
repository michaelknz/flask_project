from flask import Flask
from forms import EnterForm
from flask import render_template,request,flash
from models import User
from models import db

class Enter:
    def __init__(self):
        pass
    def RenderEnterPage(self):
        form = EnterForm()
        return render_template('enter/enter.html', title='Enter', form=form)