from flask import render_template

class Profile:
    def __init__(self):
        pass
    def Render_Profile(self):
        return render_template('profile/profile.html')
