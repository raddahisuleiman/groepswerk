
from create import db
from bp_book.model_book import Book
from bp_author.model_author import Author
class AuthorController():
    
    def create(self):
        return Author()
    
    def get(self,id):
        return Author.query.get(id)
    
    def get_all(self):
        return db.session.query(Author).order_by(Author.id.asc()).all()
    
    def does_book_exist(self,id):
        return db.session.query(Author).filter(Author.id==id).first() is not None
author_controller = AuthorController()
    