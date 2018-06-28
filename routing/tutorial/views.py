from pyramid.view import view_config, view_defaults

@view_defaults(renderer='home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name='home')
    def home(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']

        return dict(name="Home View", first=first, last=last) 