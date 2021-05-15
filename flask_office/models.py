from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    password=db.Column(db.String(64), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    timeBT = db.Column(db.String(64), index = True, unique = False)
    misstakesBT = db.Column(db.String(64), index = True, unique = False)
    timeBM = db.Column(db.String(64), index = True, unique = False)
    misstakesBM = db.Column(db.String(64), index = True, unique = False)

    def __init__(self,nickname,password,email,timeBT,misstakesBT,timeBM,misstakesBM):
        self.nickname=nickname
        self.password=password
        self.email=email
        self.timeBT=timeBT
        self.misstakesBT=misstakesBT
        self.timeBM=timeBM
        self.misstakesBM=misstakesBM