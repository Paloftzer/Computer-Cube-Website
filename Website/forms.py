from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email
from flask import redirect, url_for

class RegisterForm(FlaskForm):
    username = StringField(label="Username: ", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email Address: ", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password: ", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password: ", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label="Username: ", validators=[DataRequired()])
    password = PasswordField(label="Password: ", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class SupportForm(FlaskForm):
    name = StringField(label="Namn", validator=[DataRequired()])
    email_address = StringField(label="Email", validators=[Email(), DataRequired()])
    subject = StringField(label="Ämne", validators=[Length(min=2, max=1024), DataRequired()])