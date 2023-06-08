from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class SearchYearForm(FlaskForm):
    year = IntegerField('amount', validators=[DataRequired()])
    submit = SubmitField('Search')
    
class MemberSignUpForm(FlaskForm):
    id = IntegerField('UserId')
    name = StringField('UserName')
    password = PasswordField('Pass')
    submit = SubmitField('Create User')

class LoginForm(FlaskForm):
    username = StringField('userName', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TitelForm(FlaskForm):
    dropdown = SelectField('Select title of the song you love:', choices=[])
    submit = SubmitField('Vote')