from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    login = StringField("Name: ", validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    cpassword = PasswordField('password', validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    remember_me = BooleanField('remember_me', default=False)

class EnterForm(FlaskForm):
    login=StringField("Name: ", validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired()])
