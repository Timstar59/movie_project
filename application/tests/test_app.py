from application import app, db
from applications.models import Film_ondemand, Films
from flask_testing import Testcase

class BaseTestcase(Testcase):

    def create_app(self):
        app.config
