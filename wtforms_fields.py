from flask_wtf import FlaskForm
# from passlib.hash import pbkdf2_sha256
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo,ValidationError,DataRequired 


class RegistrationForm(FlaskForm):

    """ RegistartionForm """

    username = StringField('username', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password', validators=[InputRequired(message="password required"), Length(min=4, max=25, message="password must be between 4 and 25 characters")])
    confirm_password = PasswordField('confirm-password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit= SubmitField('Create')

 
class LoginForm(FlaskForm):
    """ login form """
    username = StringField('username', validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')