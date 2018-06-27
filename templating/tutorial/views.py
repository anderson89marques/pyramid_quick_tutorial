from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.jinja2')
def home_view(request):
    return dict(name="Home View") 


@view_config(route_name='hello', renderer='hello.jinja2')
def hello_world(request):
    return dict(name="Hello View")