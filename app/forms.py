from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class SearchYearForm(FlaskForm):
    year = IntegerField('amount', validators=[DataRequired()])
    submit = SubmitField('Search')
    
