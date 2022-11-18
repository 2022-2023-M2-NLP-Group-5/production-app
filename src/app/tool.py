from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired

langs = ["Cantonese", "English", "French", "Vietnamese"]
#years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019"]

class Analogy(FlaskForm):  # TODO change the name 
    language = SelectField('Select a language', choices=langs, validators=[DataRequired()])
    input = StringField('Enter a word', validators=[DataRequired()])
    #year1 = SelectField('Select the starting year', choices=years, validators=[DataRequired()])
    #year2 = SelectField('Select the finishing year', choices=years, validators=[DataRequired()])
    # TODO make sure that the user input a year bigger in year2 than year1
    submit = SubmitField('Go!')
