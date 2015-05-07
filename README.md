# data.ilri.org Web Application
Search application behind the landing page for ILRI's data resources.

![dataDotILRIApp screenshot](/screenshot.png?raw=true "Screenshot")

You can view the site at [https://data.ilri.org](https://data.ilri.org).

## Technology
This site was built using:

- [Bootstrap](http://getbootstrap.com/), the HTML, CSS, and JS framework.
- [Font Awesome](http://fortawesome.github.io/Font-Awesome/), the iconic font and CSS toolkit.
- [Python 2.7.x](https://www.python.org/), a widely used general-purpose programming language.
- [Pyramid](http://www.pylonsproject.org/), a web application framework for Python.
- [Jinja2](http://jinja.pocoo.org/), a template engine for the Python programming language.
- [Fanstatic](http://www.fanstatic.org/), a resource injection framework for Python.

## Building and testing
To build this site for local viewing or development:

    $ git clone https://github.com/ilri/data.ilri.org-app.git
    $ cd data.ilri.org-app
    $ virtualenv myVirtualEnv
    $ . ./myVirtualEnv/bin/activate
    $ pip install -r ./requirements.txt
    $ python setup.py develop
    $ pserve ./development.ini

The site will then be available on your local machine at: [http://localhost:6543/](http://localhost:6543/).

## License
This repository contains the code of:

- [Bootstrap](http://getbootstrap.com) which is licensed under the [MIT license](https://raw.githubusercontent.com/twbs/bootstrap/master/LICENSE).
- [Font Awesome](http://fortawesome.github.io/Font-Awesome/) which is licensed under the [MIT license](http://opensource.org/licenses/mit-license.html).


Otherwise, the contents of this application is [GPL V3](http://www.gnu.org/copyleft/gpl.html).
