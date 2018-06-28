from pyramid.view import view_config, view_defaults


@view_defaults(renderer='home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request
    
    @property
    def counter(self):
        session = self.request.session
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1
        return session

    @view_config(route_name='home')
    def home(self):
        return dict(name="Home View") 

    @view_config(route_name='hello')
    def hello(self):
        return dict(name="Hello View")