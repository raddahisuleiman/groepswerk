from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect





db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config=None):
    marketapp = Flask(__name__)
    
    if config is None:
        marketapp.config.from_object('app_config.DevConfig')

    db.init_app(marketapp)
    login_manager.init_app(marketapp)
    csrf = CSRFProtect(marketapp)
    login_manager.login_view = 'bp_user.login'

        
    register_blueprints(marketapp)
    
    return marketapp
    
def register_blueprints(marketapp):
    from bp_book import bp_book
    from bp_author import bp_author
    from bp_user import bp_user
    
    marketapp.register_blueprint(bp_book)
    marketapp.register_blueprint(bp_author)
    marketapp.register_blueprint(bp_user)


    
    