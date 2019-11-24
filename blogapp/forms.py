from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired(), Length(min=3,max=20)])
    
    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])

    confirmPassword = PasswordField('Confirm password', validators=[DataRequired(),EqualTo(password)])

    submit = SubmitField('Sign in')


class LogForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('remember me')

    submit = SubmitField('Login')