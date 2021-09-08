from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError

class Filmform(FlaskForm):
    movie_name = StringField('movie Name')
    movie_genre = IntegerField('movie genre')
    movie_rating = IntegerField('movie rating')
    director = StringField('Director name')
    release_date = DateField('Realease date')
    movie_id = IntegerField('Film number')
    submit = SubmitField('submit')
    
class read_Filmform(FlaskForm):
    movie = SelectField('movie')
