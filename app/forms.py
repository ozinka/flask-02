from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('First and Last Names', validators=[DataRequired(), Length(min=2, max=20)])
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')
    avatar = FileField('Load Avatar')
