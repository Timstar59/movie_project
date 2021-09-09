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
        n_movie_id = form.movie_id.data
        movies = Films(movie_name=n_movie_name, movie_genre=n_movie_genre, movie_rating=n_movie_rating, director=n_director, release_date=n_release_date, fk_movie_id=n_movie_id)
        db.session.add(movies)
        db.session.commit()
        return redirect(url_for('movies'))
    return render_template('add_movie.html', form=form)

@app.route('/delete/<int:id>', methods =['GET','POST'])
def delete(id):
    films_to_delete = Films.query.get(id)
    db.session.delete(films_to_delete)
    db.session.commit()
    return redirect(url_for('movies'))


@app.route('/update/<int:id>', methods =['GET', 'POST'])
def update(id):
    film = Filmform
    film_to_update = Films.query(id)
    if request.method == "POST":
        film_to_update.movie_name = request.Filmform['movie_name']
        film_to_update.movie_genre = request.Filmform['movie_genre']
        film_to_update.movie_rating = request.Filmform['movie_rating']
        film_to_update.director = request.Filmform['director']
        film_to_update.release_date = request.Filmform['release_date']
        db.session.comit()
        return redirect(url_for('movies'))

    
        

