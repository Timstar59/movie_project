from aplication import db

class Film_ondemand(db.Model):
    id = db.column(db.Integar, nullable=False, primary_key=True, unique=True)
    movie_in_cinema = db.column(db.Boolean)
    new_movies = db.column(db.String(60), nullable=False)
    movie_name = db.column(db.String(60), nullale=False)

class Films(db.Model):
    id = db.column(db.Integer, nullable=False, primary_key=True)
    movie_name = db.column(db.String(60), nullable=False, foreign_key=True)
    movie_genre = db.column(db.String(30))
    movie_rating = db.column(db.Float, nullable=False)
    director = db.column(db.String(60))
    release_date = db.column(db.DateTime)