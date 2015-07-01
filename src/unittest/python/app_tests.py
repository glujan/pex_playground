import unittest

from pex_playground import app


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        assert 'Hello World' in rv.data

    def test_bye(self):
        rv = self.app.get('/bye')
        assert 'Bye' in rv.data
