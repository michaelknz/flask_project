import consts
from flask import Flask,render_template,redirect,url_for

class Disauth:
    def __init__(self):
        pass
    def RenderDisauth(self):
        consts.is_auth=False
        consts.user=0
        return redirect(url_for('main_page'))