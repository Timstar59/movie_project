from application import db

class Film_ondemand(db.Model):
    movie_id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    movie_incinema = db.Column(db.Boolean)
    new_movies = db.Column(db.String(60))
    

class Films(db.Model):
    movie_id = db.Column(db.Integer, nullable=False, primary_key=True)
    movie_name = db.Column(db.String(60), nullable=False)
    movie_genre = db.Column(db.String(30))
    movie_rating = db.Column(db.Float)
    director = db.Column(db.String(60))
    release_date = db.Column(db.DateTime)
    fk_movie_id = db.Column(db.Integer, db.ForeignKey('film_ondemand.movie_id'), nullable=False)
    

