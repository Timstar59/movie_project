from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Film_ondemand, Films
from application.forms import FlaskForm, Filmform

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movies')
def movies():
    movies = Films.query.all()
    return render_template('movies.html', movies = movies)
    
@app.route('/add_movie', methods=['GET', 'POST'])
def add():
    form = Filmform()

    if request.method == "POST":
        n_movie_name = form.movie_name.data
        n_movie_genre = form.movie_genre.data
        n_movie_rating = form.movie_rating.data
        n_director = form.director.data
        n_release_date = form.release_date.data
        movies = Films(movie_name=n_movie_name, movie_genre=n_movie_genre, movie_rating=n_movie_rating, director=n_director, release_date=n_release_date)
        db.session.add(movies)
        db.session.commit()
        return redirect(url_for('movies'))
    return render_template('add_movie.html', form=form)


