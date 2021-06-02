from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='user_name')
    first_name = StringField(label='first_name')
    last_name = StringField(label='last_name')
    password_1 = PasswordField(label='password_1')
    password_2 = PasswordField(label='password_2')
    submit = SubmitField(label='submit')
