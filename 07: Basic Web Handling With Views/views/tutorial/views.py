from pyramid.response import Response
from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home')
def home(request):
    return Response('<body>Visit <a href="/howdy">hello</a></body>')
