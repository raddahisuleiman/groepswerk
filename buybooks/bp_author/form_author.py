from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField,BooleanField

class AuthorForm(FlaskForm):
    firstname = StringField('firstname', id='author_first_name')
    lastname = StringField('lastname', id='author_lastname')
    submit = SubmitField('Save', id='blog_submit')


