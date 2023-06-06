from functools import wraps
from flask import abort
from flask_login import current_user
from create import login_manager, db
from bp_user.model_user import User
from typing import Optional, Union
from typing import Optional, Tuple, List


class ControllerUsers:
    """
    A class that handles operations related to users.
    """

    def get(self, id: int) -> Optional[User]:
        """
        Retrieve a user by their ID.

        Args:
            id (int): The ID of the user to retrieve.

        Returns:
            Optional[User]: The user object with the specified ID, or None if not found.
        """
        return User.query.get(id)

    def get_all(self) -> List[User]:
        """
        Retrieve all users.

        Returns:
            List[User]: A list of all user objects.
        """
        return db.session.query(User).all()

    def email_exists(self, email: str) -> bool:
        """
        Check if a user with the specified email exists.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the user with the email exists, False otherwise.
        """
        user = db.session.query(User).filter(User.email == email.lower()).first()
        return (user is not None)

    def update(self, obj: Optional[User], name: str, email: str, pwd: str = '', profile_type: int = 1) -> User:
        """
        Update or create a user with the provided details.

        Args:
            obj (Optional[User]): The user object to update. If None, a new user will be created.
            name (str): The name of the user.
            email (str): The email of the user.
            pwd (str): The password of the user. Defaults to an empty string.
            profile_type (int): The profile type of the user. Defaults to 1.

        Returns:
            User: The updated or newly created user object.
        """
        if obj is None:
            obj = User()

        obj.name = name
        obj.email = email
        obj.set_password(pwd)
        obj.profile_type = profile_type
        db.session.add(obj)
        db.session.commit()

        return obj

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            Optional[User]: The user object with the specified email, or None if not found.
        """
        if email is None or email == '':
            return None

        user = db.session.query(User).filter(User.email == email.lower()).first()
        return user

    def change_pass(self, userid: int, pwd: str) -> bool:
        """
        Change the password of a user.

        Args:
            userid (int): The ID of the user.
            pwd (str): The new password.

        Returns:
            bool: True if the password change is successful, False otherwise.
        """
        user = self.get(userid)
        if user is not None:
            user.set_password(pwd)
            db.session.add(user)
            db.session.commit()
            return True

        return False

    def register_user(self, email: str, password: str) -> Tuple[bool, Optional[User]]:
        """
        Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            Tuple[bool, Optional[User]]: A tuple containing a boolean indicating the success of the registration
            and the registered user object if successful, or None otherwise.
        """
        if email is None or email == '':
            return False, None

        email = email.lower()

        if not self.email_exists(email):
            user = self.update(None, '', email, password)
            return (user is not None), user

        return False, None

    def register_admin(self, email: str, password: str) -> Tuple[bool, Optional[User]]:
        """
        Register a new admin user.

        Args:
            email (str): The email of the admin user.
            password (str): The password of the admin user.

        Returns:
            Tuple[bool, Optional[User]]: A tuple containing a boolean indicating the success of the admin registration
            and the registered admin user object if successful, or None otherwise.
        """
        if email is None or email == '':
            return False, None

        email = email.lower()

        if not self.email_exists(email):
            user = self.update(None, '', email, password, 0)
            return (user is not None), user

        return False, None


users_controller = ControllerUsers()
