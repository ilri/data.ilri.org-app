from pyramid.view import view_config
from resources import basicCSS


@view_config(route_name='home', renderer='templates/index.html')
def index(request):
    basicCSS.need()
    return {}

@view_config(route_name='rdm', renderer='templates/RDM/rdm.html')
def rdm(request):
    basicCSS.need()
    return {}

@view_config(route_name='rdmdocs', renderer='templates/RDM/rdmdocs.html')
def rdmdocs(request):
    basicCSS.need()
    return {}

@view_config(route_name='meta', renderer='templates/RDM/meta.html')
def meta(request):
    basicCSS.need()
    return {}

@view_config(route_name='odktools', renderer='templates/RDM/odktools.html')
def odktools(request):
    basicCSS.need()
    return {}
