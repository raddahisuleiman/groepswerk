from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, BooleanField,SelectField,TextAreaField
from utils import book_genres, book_types

class BookForm(FlaskForm):
    title = StringField('Title', id='book_title')
    ISBN = StringField('ISBN', id='book_isbn')
    type = SelectField('Type', id='book_type', choices=book_types)
    file = FileField('File', id='File')
    genre = SelectField('genre', choices=book_genres)
    desc = TextAreaField('desc')
    add_author = BooleanField('Add Author')
    
    firstname = StringField('firstname', id='author_first_name')
    lastname = StringField('lastname', id='author_lastname')
    
    submit = SubmitField('Save', id='blog_submit')
    
class AddForm(FlaskForm):
    submit = SubmitField(label='add')

    


