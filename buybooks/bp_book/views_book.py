from flask import render_template, abort, redirect, url_for, send_file, current_app, request, flash
from bp_book import bp_book
from bp_author import bp_author
from bp_book.form_book import BookForm, AddForm
from bp_book.controller_book import book_controller
from bp_author.controller_author import author_controller
import os
from bp_user import bp_user
from create import db
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from typing import Union

def allowed_image(filename: str) -> bool:
    """
    Check if the given filename has an allowed image extension.

    Args:
        filename (str): The name of the file.

    Returns:
        bool: True if the file has an allowed image extension, False otherwise.
    """
    if not '.' in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in current_app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


@bp_book.route('/add', methods=['GET', 'POST'])
@login_required
def do_home() -> Union[str, redirect]:
    """
    Route for adding a book.

    Returns:
        Union[str, redirect]: The rendered template or a redirect to the market page.
    """

    formbook = BookForm()

    book = book_controller.create()
    author = author_controller.create()

    if formbook.validate_on_submit():

        dir = os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER'])

        book.title = formbook.title.data
        book.isbn = formbook.ISBN.data
        book.type = formbook.type.data
        book.genre = formbook.genre.data
        book.description = formbook.desc.data
        author.firstname = formbook.firstname.data
        author.lastname = formbook.lastname.data

        if request.files:
            image = formbook.file.data
            print(f'dit is de image {image}')

            if image.filename == '':
                flash('No photo added')
                return redirect(request.url)
            if not allowed_image(image.filename):
                print('image not allowed')
                return redirect(request.url)
            else:
                filename = image.filename
                image.save(os.path.join(os.path.abspath("static"), filename))
                book.photo = filename

            book.owner = author

            db.session.add(author)
            db.session.add(book)
            db.session.commit()

            return redirect(url_for('bp_book.do_market'))

    return render_template('home.html', form=formbook)


@bp_book.route('/market', methods=['GET', 'POST'])
def do_market() -> str:
    """
    Route for displaying the book market.

    Returns:
        str: The rendered template.
    """
    addform = AddForm()
    books = book_controller.get_all()

    if request.method == "POST":
        id = request.form.get('added_book')
        book = book_controller.get(id)
        user = current_user
        print(user)

    return render_template('market.html', books=books, addform=addform)
