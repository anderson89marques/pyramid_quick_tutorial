from pyramid.view import view_config, view_defaults


@view_defaults(renderer='home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name='home')
    def home(self):
        return dict(name="Home View") 

    @view_config(route_name='hello')
    @view_config(route_name='hello_json', renderer='json')
    def hello(self):
        return dict(name="Hello View")