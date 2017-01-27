from flask_sqlalchemy import SQLAlchemy
from flask_login import AnonymousUserMixin
# from jmilkfansblog import app
from uuid import uuid4
from jmilkfansblog.extensions import bcrypt

db = SQLAlchemy()

posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

users_roles = db.Table('users_roles',
                       db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
                       db.Column('role_id', db.String(45), db.ForeignKey('roles.id')))

class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic'
    )

    roles = db.relationship(
        'Role',
        secondary = users_roles,
        backref = db.backref('users', lazy='dynamic'))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = self.set_password(password)

        # Setup the default-role for user.
        default = Role.query.filter_by(name="default").one()
        # default = Role.query.filter_by(name="default").first()
        self.roles.append(default)

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)

    def set_password(self, password):
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active():
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return unicode(self.id)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Role '{}'>".format(self.name)





class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreigin key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic'
    )

    # many to many: posts <==> tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "<Model Post '{}'>".format(self.title)

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.id = str(uuid4())
        self.name = name

    def __repr__(self):
        return '<Model Tag {}>'.format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self):
        self.id = str(uuid4())

    def __repr__(self):
        return '<Model Comment {} >'.format(self.name)

class BrowseVolume(db.Model):
    """Represents Proected browse_volumes."""

    __tablename__ = 'browse_volumes'
    id = db.Column(db.String(45), primary_key=True)
    home_view_total = db.Column(db.Integer)

    def __init__(self):
        self.id = str(uuid4())
        self.home_view_total = 0


    def __repr__(self):
        return '<Model BrowseVolume `{}`>'.format(self.home_view_total)

    def add_one(self):
        self.home_view_total += 1


class Reminder(db.Model):
    """Represents Proected reminders."""

    __tablename__ = 'reminders'
    id = db.Column(db.String(45), primary_key=True)
    date = db.Column(db.DateTime())
    email = db.Column(db.String(255))
    text = db.Column(db.Text())

    def __init__(self):
        self.id = str(uuid4())

    def __repr__(self):
        return '<Model Reminder `{}`>'.format(self.text[:20])