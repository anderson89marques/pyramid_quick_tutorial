import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
    
    def test_home(self):
        from tutorial.views import home_view

        request = testing.DummyRequest()
        response = home_view(request)
        # Our view now returns data
        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from tutorial.views import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual('Hello View', response['name'])

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp
        
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Home View', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<h1>Hello View', res.body)