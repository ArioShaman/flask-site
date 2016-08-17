from flask.ext.wtf import Form 
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from app.models import User
#class LoginForm(Form):
	#username = StringField('Username',[validators.Length(min=4, max=25)])



class RegistrationForm(Form):
    first_last_name = StringField('FIO',[validators.Length(min = 10, max = 24)],render_kw={"placeholder": "Enter your last and first Name"})
    nickname = StringField('nickname', [validators.Length(min = 4, max = 25)],render_kw={"placeholder": "Enter your Email"})
    email = StringField('Email Address', [validators.Length(min = 6, max = 35)],render_kw={"placeholder": "Enter your Email"})
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ],render_kw={"placeholder": "Enter your password"})
    confirm = PasswordField('Repeat Password',render_kw={"placeholder": "Confirm your password"})
    
class LoginForm(Form):
	username = StringField('Username',[validators.Required()],render_kw={"placeholder": "Enter your username"})
	password = PasswordField('Password',[validators.Required()],render_kw={"placeholder": "Enter your password"})
    
