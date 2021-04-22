from flask import render_template

class Error:
    def __init__(self, *args, **kwargs):
        pass
    def existing_login(self):
        return render_template('error/existing_login.html')
    def existing_email(self):
        return render_template('error/existing_email.html')
    def different_passwords(self):
        return render_template('error/different_passwords.html')
    def login_does_not_exist(self):
        return render_template('error/login_not_exist.html')
    def wrong_password(self):
        return render_template('error/wrong_password.html')