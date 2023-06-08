from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class SearchYearForm(FlaskForm):
    year = IntegerField('amount', validators=[DataRequired()])
    submit = SubmitField('Search')
    
class CreateUserForm(FlaskForm):
    id = IntegerField('UserId', validators=[DataRequired()])
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create User')

class LoginForm(FlaskForm):
    username = StringField('userName', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')