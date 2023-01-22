from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired

langs = ["English", "German"]

class Analogy(FlaskForm):  
    language = SelectField('Select a language', choices=langs, validators=[DataRequired()])
    input = StringField('Enter a word', validators=[DataRequired()])
    submit = SubmitField('Go!')
