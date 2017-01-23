from flask import Flask, redirect, url_for

# from config import DevConfig
from jmilkfansblog.controllers import blog
from jmilkfansblog.models import db
from jmilkfansblog.extensions import bcrypt

def create_app(object_name):

    app = Flask(__name__)
    # views = __import__('views')
    app.config.from_object(object_name)
    db.init_app(app)
    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog.blog_blueprint)

    return app




# if __name__ == '__main__':
#
#     app.run(debug=True)