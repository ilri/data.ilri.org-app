from fanstatic import Library
from fanstatic import Resource
from fanstatic import Group


library = Library('datailriorgapp', 'resources')

basicCSSArray = []
basicCSSArray.append(Resource(library, 'css/bootstrap.min.css'))
basicCSSArray.append(Resource(library, 'css/ilri.css'))
basicCSSArray.append(Resource(library, 'fa/css/font-awesome.css'))
basicCSS = Group(basicCSSArray)

def pserve():
    """A script aware of static resource"""
    import pyramid.scripts.pserve
    import pyramid_fanstatic
    import os

    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname, 'resources')
    pyramid.scripts.pserve.add_file_callback(
                pyramid_fanstatic.file_callback(dirname))
    pyramid.scripts.pserve.main()
