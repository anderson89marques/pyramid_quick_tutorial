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
        self.assertEqual(response.status_code, 200)
    
    def test_home_content(self):
        from tutorial.views import home_view

        request = testing.DummyRequest()
        response = home_view(request)
        self.assertIn(b'Visit', response.body)

    def test_hello(self):
        from tutorial.views import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
    
    def test_hello_content(self):
        from tutorial.views import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertIn(b'Go back', response.body)



class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp
        
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<body>Visit', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<body>Go back', res.body)