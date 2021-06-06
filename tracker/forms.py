from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from tracker.models import User


class RegisterForm(FlaskForm):

    #   check to see if there is already a username with the provided data in the database
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    first = StringField(label='First Name', validators=[Length(min=1), DataRequired()])
    last = StringField(label='Last Name', validators=[Length(min=1), DataRequired()])
    password_1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):

    username = StringField(label='User Name: ', validators=[DataRequired()])
    password = PasswordField(label='Password: ', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


class EnterDataForm(FlaskForm):
    #   check to see if there is already a username with the provided data in the database
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    submit = SubmitField(label='Enter Data')

