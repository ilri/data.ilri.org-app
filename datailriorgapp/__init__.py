from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_fanstatic')
    config.add_jinja2_renderer('.html')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('rdm', '/rdm')
    config.add_route('rdmdocs', '/rdm/docs')
    config.add_route('meta', '/rdm/meta')
    config.add_route('odktools', '/rdm/odktools')

    templatesPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    config.add_jinja2_search_path(templatesPath)

    config.scan()
    return config.make_wsgi_app()
