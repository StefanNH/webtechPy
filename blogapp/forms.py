from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from blogapp.models import User

class RegForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3,max=20)])
    
    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])

    confirm = PasswordField('Confirm password', validators=[DataRequired()])

    submit = SubmitField('Sign in')

    def ValidateUsername(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use, please choose different username')
    def ValidateEmail(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use, please choose different email')

class LogForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('remember me')

    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')