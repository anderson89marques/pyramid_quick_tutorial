import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
    
    def test_home(self):
        from tutorial.views import TutorialViews

        request = testing.DummyRequest()
        request.matchdict['first'] = 'Anderson'
        request.matchdict['last'] = 'Marques'
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual('Anderson', response['first'])
        self.assertEqual('Marques', response['last'])

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp
        
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/howdy/Anderson/Marques', status=200)
        self.assertIn(b'Anderson', res.body)
        self.assertIn(b'Marques', res.body)