from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    login = StringField("Name: ", validators=[DataRequired()])
    password = StringField("Name: ", validators=[DataRequired()])
    cpassword = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    remember_me = BooleanField('remember_me', default=False)
