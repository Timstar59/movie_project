from aplication import db

class Film_ondemand(db.Model):
    id = db.column(db.Integar, primary_key =True)
    new_customer = db.column(db.Boolean)
    new_movies = db.column(db.string(60), nullable=False)
    movie_name = db.column(db.string(60), nullale=False)