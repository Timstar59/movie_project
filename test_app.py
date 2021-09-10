from application import app, db
from application.models import Film_ondemand, Films
from flask_testing import TestCase 
from flask import url_for 

class TestBase(TestCase):

     def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///', MY_SECRET_KEY='SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app
    
     def setUp(self):
         db.create_all()
         db.session.commit()

     def tearDown(self):
         db.session.remove()
         db.drop_all

class TestViews(TestBase):
     def test_home_get(self):
         response = self.client.get(url_for('home'))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'Index', response.data)

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

class TestViewsdelete(TestBase):
     def test_movies_delete(self):
         response = self.client.get(url_for('delete'))
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'movies', response.data)


#class TestAdd(TestBase):
   # def test_add_post(self):
        #response =self.client.post(url_for('add'),
        #data = dict(movie_name= 'newWanted',
        #movie_genre = 'action', movie_rating = 5, director = 'Andy', release_date='1998-02-03', fk_movie_id='99'),
        #follow_redirects=True
        #)

#class TestDelete(Test):
    #def test_delete_
    