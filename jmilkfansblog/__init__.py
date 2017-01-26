from flask import Flask, redirect, url_for

# from config import DevConfig
from jmilkfansblog.controllers import blog, main
from jmilkfansblog.models import db
from jmilkfansblog.extensions import bcrypt, login_manager, principals

from flask_login import current_user
from flask_principal import identity_loaded, UserNeed, RoleNeed

def create_app(object_name):

    app = Flask(__name__)
    # views = __import__('views')
    app.config.from_object(object_name)
    db.init_app(app)
    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)

    # Init the Flask-Login via app object
    login_manager.init_app(app)
    # Init the Flask-Prinicpal via app object
    principals.init_app(app)

    # @app.route('/')
    # def index():
    #     return redirect(url_for('blog.home'))

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """Change role via add the Need object into Role.
           Need the access the app object.
        """

        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity user object
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity user object
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app




# if __name__ == '__main__':
#
#     app.run(debug=True)