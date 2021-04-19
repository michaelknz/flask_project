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