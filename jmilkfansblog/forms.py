from flask_wtf import Form, RecaptchaField, FlaskForm
from wtforms import (StringField,
                     TextField,
                     TextAreaField,
                     PasswordField,
                     BooleanField,
                     ValidationError
                     )
from wtforms.validators import DataRequired, Length, EqualTo, URL
import re
from jmilkfansblog.models import User

# from wtforms import ValidationError

class CommentForm(Form):

    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextField(u'Comment', validators=[DataRequired()])

class LoginForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")

    def validate(self):
        check_validata = super(LoginForm, self).validate()

        if not check_validata:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password.')
            return False
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password.')
            return False

        return True

class RegisterForm(Form):
    """Register Form."""

    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField()

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        # If validator no pass
        if not check_validate:
            return False

        # Check the user whether exist
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('User with that name already exists.')
            return False
        return True

class PostForm(Form):
    """Post Form."""
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])

def custom_email(form_object, field_object):

    if not re.match(r"[^@+@[^@]+\.[^@]]+", field_object.data):
        raise ValidationError('Field must be a valid email address.')