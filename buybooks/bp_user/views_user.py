from bp_user import bp_user
from flask import render_template, abort, redirect, url_for, send_file, current_app, request, flash
from bp_user.form_user import UserLoginForm, UserRegistrationForm
from bp_user.controller_user import users_controller
from flask_login import login_user, current_user, logout_user
from create import db
from bp_user.model_user import User
import logging


@bp_user.route("/login", methods=["GET", "POST"])
def login():
    """
    User login route.

    Renders the login form and handles form submission for user authentication.

    Returns:
        If the form submission is successful and the user is authenticated, redirects to the market page.
        Otherwise, renders the login form.
    """
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if not user.check_password(form.password.data):
                flash('Wrong password', category='warning')
            else:
                # In case we have another user still logged in
                if current_user and current_user.is_authenticated:
                    try:
                        current_user.authenticated = False
                        db.session.add(current_user)
                        db.session.commit()
                        logout_user()
                    except Exception as e:
                        # If this fails, we do not care, but we certainly do not want to block someone logging in
                        logging.info('Error during login (logout): {}'.format(e))

                # Now set the new user to authenticated
                user.authenticated = True
                db.session.add(user)
                db.session.commit()

                # Do the actual login
                login_user(user)

                flash('You are now logged in', category='success')

                return redirect(url_for('bp_book.do_market'))
        else:
            flash('User not found', category='warning')

    return render_template('login.html', form=form)


@bp_user.route('/register', methods=['GET', 'POST'])
def do_register():
    """
    User registration route.

    Renders the registration form and handles form submission for user registration.

    Returns:
        If the form submission is successful and a new user is registered, redirects to the market page.
        Otherwise, renders the registration form.
    """
    form = UserRegistrationForm()
    if form.validate_on_submit():
        result, user = users_controller.register_user(form.email.data, form.password.data)
        if result and user is not None:
            flash('Created and logged in', category='info')

            login_user(user)

            return redirect(url_for('bp_book.do_market'))
        else:
            flash('User already exists', category='warning')

        return redirect(url_for('bp_user.do_register'))

    return render_template('register.html', form=form)


@bp_user.route('/register/admin', methods=['GET', 'POST'])
def do_register_admin():
    """
    Admin registration route.

    Renders the admin registration form and handles form submission for admin registration.

    Returns:
        If the form submission is successful and a new admin user is registered, redirects to the home page.
        Otherwise, renders the admin registration form.
    """
    db.create_all()

    form = UserRegistrationForm()
    if form.validate_on_submit():
        result, user = users_controller.register_admin(form.email.data, form.password.data)
        if result and user is not None:
            flash('Created admin', category='info')

            login_user(user)

            return redirect(url_for('bp_book.do_home'))
        else:
            flash('User already exists', category='warning')

        return redirect(url_for('bp_user.do_register_admin'))

    return render_template('register.html', form=form)


@bp_user.route('/logout')
def logout():
    """
    User logout route.

    Logs out the current user and redirects to the login page.

    Returns:
        Redirects to the login page after logging out the user.
    """
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('bp_user.login'))
