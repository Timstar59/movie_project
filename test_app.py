from application import app, db
import pytest
from application.models import Film_ondemand, Films
from flask_testing import TestCase 
from flask import url_for 

class TestBase(TestCase):

     def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///', MY_SECRET_KEY='SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app
    
     def setUp(self):
         db.create_all()
         test_film = Films(movie_name='hotel',movie_genre = 'action', movie_rating='9',director ='sandy',release_date='1998-04-')
         db.session.commit()

     def tearDown(self):
         db.session.remove()
         db.drop_all

class TestHomeAdd(TestBase):
    def test_add_new_home(self):
        with self.client:
            self.client.post(url_for('add'),
                data.dict( 
                    movie_id ='2',
                    movie_incinema = True,
                    new_movie = True
             ),
             follow_redirects = True)
        response = self.client.post(url_for('add'),
        )
        


class TestViewshome(TestBase):
     def test_home_get(self):
         response = self.client.get(url_for('home'))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'Index', response.data)

class Test_empty_db(TestBase):
    def test_empty_db(self):
        response = self.client.get('/')
        self.assertIn(b'no entry in here' in response.data)


class TestViews1(TestBase):
     def test_movies_get(self):
         response = self.client.get(url_for('movies'))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'movies', response.data)

class TestViewsadd(TestBase):
     def test_movies_get(self):
         response = self.client.get(url_for('add'))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'add_movie', response.data)

class TestDelete(TestBase):
     def test_movies_delete(self):
         response = self.client.delete(
             url_for('movies'),
             data = dict(movie_id='3')
        )
        
class TestAddfilm(TestBase):
    def test_add_film(self):
        response = self.client.post(
            url_for('add'),
            data = dict(movie_name="Jumanji"),
            follow_redirects=True
        )
        self.assertIn(b'movies',response.data)

class Testupdatefilm(TestBase):
    def update_film(self):
        response = self.client.post(
            url_for('update'),
            follow_redirects=True
        )

class TestAddentry(TestBase): 
    def test_add_movie(self):
        response = self.client.post(url_for('add'),
        data = dict( movie_name = "hunter",
                     movie_genre =  "horror",
                     movie_rating = "5",
                     director = 'sandy',
                     realease_date = '2003-03-02',
                     fk_movie_id = '2'
        ), follow_redirects=True)

        self.assertIn(b"movies", response.data)
        
         


#class TestAdd(TestBase):
   # def test_add_post(self):
        #response =self.client.post(url_for('add'),
        #data = dict(movie_name= 'newWanted',
        #movie_genre = 'action', movie_rating = 5, director = 'Andy', release_date='1998-02-03', fk_movie_id='99'),
        #follow_redirects=True
        #)

#class TestDelete(Test):
    #def test_delete_
    