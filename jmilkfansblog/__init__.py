from flask import Flask, redirect, url_for
import os
# from config import DevConfig
from jmilkfansblog.controllers import blog, main
from jmilkfansblog.models import db, User, Post, Role, Tag, BrowseVolume, Reminder
from jmilkfansblog.extensions import bcrypt, login_manager, principals, flask_admin

from flask_login import current_user
from flask_principal import identity_loaded, UserNeed, RoleNeed
from jmilkfansblog.controllers.admin import CustomView, CustomModelView, PostView, CustomFileAdmin

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

    # cache.init_app(app)

    flask_admin.init_app(app)
    # Register view Function 'CustomView' into Flask-Admin
    flask_admin.add_view(CustomView(name='Custom'))
    # Register view function 'CustomModelView' into Flask-Admin
    models = [Role, Tag, Reminder, BrowseVolume, User]
    for model in models:
        flask_admin.add_view(
            CustomModelView(model, db.session, category='Models')
        )
    # Register view function 'PostView' into Flask-Admin
    flask_admin.add_view(
        PostView(Post, db.session, category='PostManager')
    )
    # Register and define path of File System for Flask-Admin
    flask_admin.add_view(
        CustomFileAdmin(
            os.path.join(os.path.dirname(__file__), 'static'),
            '/static',
            name='Static Files'
        )
    )

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