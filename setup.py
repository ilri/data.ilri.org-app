import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_fanstatic'
    ]

setup(name='data.ilri.org-app',
      version='1.0',
      description='data.ilri.org Application',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Carlos Quiros',
      author_email='c.f.quiros@cgiar.org / cquiros@qlands.com',
      url='https://data.ilri.org/',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="datailriorgapp",
      entry_points="""\
      [paste.app_factory]
      main = datailriorgapp:main
      [fanstatic.libraries]
      datailriorgapp = datailriorgapp.resources:library
      [console_scripts]
      pserve-fanstatic = datailriorgapp.resources:pserve
      """,
      )
