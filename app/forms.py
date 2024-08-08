from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('First and Last Names', validators=[DataRequired(), Length(min=2, max=20)])
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')
    avatar = FileField('Load Avatar')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Such login is already in use. Please choose a different one.')


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class': 'form-control'})


class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choices=[], render_kw={'class': 'form-control'})
