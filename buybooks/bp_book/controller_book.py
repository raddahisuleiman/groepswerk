from typing import List
from create import db
from bp_book.model_book import Book
from bp_author.model_author import Author

class BookController:
    """
    A class that handles operations related to books.
    """

    def create(self) -> Book:
        """
        Create a new book.

        Returns:
            Book: The newly created book object.
        """
        return Book()

    def get(self, id: int) -> Book:
        """
        Retrieve a book by its ID.

        Args:
            id (int): The ID of the book to retrieve.

        Returns:
            Book: The book object with the specified ID.
        """
        return Book.query.get(id)

    def get_all(self) -> List[Book]:
        """
        Retrieve all books.

        Returns:
            List[Book]: A list of all book objects.
        """
        return db.session.query(Book).order_by(Book.id.asc()).all()

    def does_book_exist(self, title: str) -> bool:
        """
        Check if a book with the specified title exists.

        Args:
            title (str): The title of the book to check

        """
        return db.session.query(Book).filter(Book.title == title).first() is not None


book_controller = BookController()
