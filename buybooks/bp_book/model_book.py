from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from create import db


class Book(db.Model):
    
    id = db.Column('id', db.Integer, primary_key=True, index=True)
    title = db.Column('title', db.String(length = 50), nullable = False)
    isbn = db.Column('isbn', db.String(15), nullable = True)
    genre = db.Column('genre', db.String(40), nullable = True)
    type = db.Column('type', db.String(25))
    photo = db.Column('photo', db.String(50))
    description = db.Column('description', db.String(150))
    owner_id = db.Column(db.Integer, db.ForeignKey('author.id'))    
    bookowner_id = db.Column(db.Integer, db.ForeignKey('t_users.pk_id'))
    def __str__(self):
        return f'{self.id} - {self.title}'
    

    

    


    

    
    



