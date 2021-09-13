from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError

class Filmform(FlaskForm):
    movie_name = StringField('movie Name', validators=[DataRequired()])
    movie_genre = StringField('movie genre', validators=[DataRequired()])
    movie_rating = IntegerField('movie rating', validators=[DataRequired()])
    director = StringField('Director name', validators=[DataRequired()])
    release_date = DateField('Realease date')
    movie_id = IntegerField('Film number', validators=[DataRequired()])
    submit = SubmitField('submit')
    
class Film_ondemandform(FlaskForm):
    movie_id = IntegerField('Film id')
    movie_incinema = BooleanField(' Is Film in cinema')
    new_movie = BooleanField('New Film?' )
    submit = SubmitField('submit')

