from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    user_name = StringField(label='User Name')
    first_name = StringField(label='First Name')
    last_name = StringField(label='Last Name')
    password_1 = PasswordField(label='Password:')
    password_2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')
