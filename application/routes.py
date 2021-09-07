from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Film_ondemand, Films
from application.forms import FlaskForm 

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = Filmform()

    if request.method == "POST":
        movie_name = form.movie_name.data
        movie_genre = form.movie_genere.data
        movie_rating = form.movie_rating.data
        director = form.director.data
        in_cinema = form.in_cinema.data
    
    return render_template('home.html', form=form)


