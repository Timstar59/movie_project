from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class Filmform(FlaskForm):
    movie_name = StringField('movie Name')
    movie_genre = IntegerField('movie genre')
    movie_rating = IntegerField('movie rating')
    director = StringField('Director name')
    in_cinema = SelectField('in cinema', choices=[
        ('yes','Yes'),
        ('no', 'No'),
        ('')
    ])
    submit = SubmitField('submit')
    

