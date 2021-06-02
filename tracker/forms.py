from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    user_name = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    first_name = StringField(label='First Name', validators=[Length(min=1), DataRequired()])
    last_name = StringField(label='Last Name', validators=[Length(min=1), DataRequired()])
    password_1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Account')
