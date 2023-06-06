from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from create import db


class Author(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, index=True)
    firstname = db.Column('f_firstname', db.String(length = 50), nullable = False)
    lastname = db.Column('f_lastname', db.String(50), nullable = False)
    email = db.Column('f_email', db.String(10))
    books = db.relationship('Book', backref='owner', lazy=True)
    
    
    def __str__(self):
        return f'{self.firstname} - {self.lastname}'