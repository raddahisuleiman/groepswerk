from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class UserLoginForm(FlaskForm):
    email = EmailField('Login', id='login_email')
    password = PasswordField('Password', id='login_pwd')
    remember_me = BooleanField('Keep me logged in', id='login_remember_me')    
    submit = SubmitField('Submit', id="login_submit")
 

class UserRegistrationForm(FlaskForm):
    email = EmailField('Email', id='register_email', validators=[DataRequired()])
    password = PasswordField('Password', id='register_pwd1', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', id='register_pwd2', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register', id="register_submit")
