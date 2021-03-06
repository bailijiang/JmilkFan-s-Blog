from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import session
from flask_principal import Principal, Permission, RoleNeed
from flask_cache import Cache
from flask_admin import Admin
from flask_restful import Api

# Create the Flask-Bcrypt's instance
bcrypt = Bcrypt()

login_manager = LoginManager()
principals = Principal()

# cache = Cache()

flask_admin = Admin()

admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))

login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page."
login_manager.login_message_category = "info"

# Create the Flask-Restful's instance
restful_api = Api()

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.filter_by(id=user_id).first()