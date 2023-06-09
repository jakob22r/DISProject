from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo

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

class TitelForm(FlaskForm):
    dropdown = SelectField('Select title of the song you love:', choices=[])
    submit = SubmitField('Vote')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()], render_kw={"class": "static/left-align"})
    new_password = PasswordField('New Password', validators=[DataRequired()], render_kw={"class": "left-align"})
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), 
        EqualTo('new_password', message='Passwords must match')], render_kw={"class": "static/left-align"})
    submit = SubmitField('Apply changes')