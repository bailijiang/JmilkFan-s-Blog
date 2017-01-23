from flask_wtf import Form
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

def custom_email(form_object, field_object):

    if not re.match(r"[^@+@[^@]+\.[^@]]+", field_object.data):
        raise ValidationError('Field must be a valid email address.')