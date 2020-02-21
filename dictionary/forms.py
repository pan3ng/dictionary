from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')
