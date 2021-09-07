from application import db
db.drop_all()
db.create_all()

#testuser = Films(movie_name='Grooty',movie_genre='Toot') # Extra: this section populates the table with an example entry
#db.session.add(testuser)
#db.session.commit()