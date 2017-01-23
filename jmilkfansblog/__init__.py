from flask import Flask, redirect, url_for

from config import DevConfig
from controllers import blog
from models import db

app = Flask(__name__)
# print(app.config)


# views = __import__('views')

app.config.from_object(DevConfig)


db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('blog.home'))

app.register_blueprint(blog.blog_blueprint)

if __name__ == '__main__':

    app.run(debug=True)