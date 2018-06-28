import logging
from pyramid.view import view_config, view_defaults

log = logging.getLogger(__name__)

@view_defaults(renderer='home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name='home')
    def home(self):
        log.debug('In home view')
        return dict(name="Home View") 

    @view_config(route_name='hello')
    def hello(self):
        log.debug('In hello view')
        return dict(name="Hello View")