from application import db

class Film_ondemand(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    movie_incinema = db.column(db.Boolean)
    new_movies = db.Column(db.String(60), nullable=False)
    movie_name = db.Column(db.String(60), nullable=False)

class Films(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    movie_name = db.Column(db.String(60), nullable=False)
    movie_genre = db.Column(db.String(30))
    movie_rating = db.Column(db.Float, nullable=False)
    director = db.Column(db.String(60))
    release_date = db.Column(db.DateTime)