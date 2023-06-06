from aifc import Error
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from sqlalchemy.orm import validates
from create import db,login_manager
from flask_login import UserMixin
import logging

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
        # return user if user and (not user.is_banned or not user.is_active) else None
    except Exception as e:
        logging.error('error loading user {}: {}'.format(user_id, e))
    return None



class User(db.Model, UserMixin):
    __tablename__ = 't_users'
    
    id = db.Column('pk_id', db.Integer, primary_key=True)
    name = db.Column('f_name', db.String(125), nullable=False)
    email = db.Column('f_email', db.String(250), nullable=False, unique=True)
    profile_type = db.Column('f_profile_type', db.Integer, default=1)
    # 0 = admin
    # 1 = user    
    active = db.Column('f_active', db.Boolean, default=True)
    pass_hashed = db.Column('f_password', db.String(125), nullable=False)
    userbooks = db.relationship('Book', backref='bookown', lazy=True)

    
    
    def __str__(self):
        return f'{self.id}: {self.email}' 
        
    @validates('email')
    def validate_email(self, key, value):
        return value.lower()
        
    def is_authenticated(self):
        return self.authenticated
    
    def is_active(self):
        return self.active
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id
    
    def set_password(self, value):
        self.pass_hashed = generate_password_hash(value)
    
    @validates
    def validate_pwd(self, key, value):
        if 'pbkdf2:sha256:' not in value:
            raise Error
        
        return value
    
    
    def check_password(self, value):
        return check_password_hash(self.pass_hashed, value)
        
    @property
    def is_author(self):
        return self.profile_type == 0
    
    @property
    def is_customer(self):
        return self.profile_type != 0