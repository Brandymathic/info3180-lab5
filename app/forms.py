# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, FileRequired, FileAllowed

class MovieForm(FlaskForm):

    title = StringField('Movie Title', validators = [DataRequired(), Length(max=100)])

    description = TextAreaField('Description', validators=[DataRequired()])

    poster = FileField('Movie Poster', validators= [FileRequired(),FileAllowed(['jpg','png','jpeg'], 'Images Only!!') ])

    submit = SubmitField('Add Movie')