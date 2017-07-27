# Majority of this assignment was put in a whole new directory.
#Just copy and pasting the work I did there, here so I can pass it to git.
try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Genessy',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'My email',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'projectname'
}
    
setup(**config)


from nose.tools import *
import NAME

def setup():
    print ('SETUP!')

def teardown():
    print ('TEAR DOWN!')

def test_basic():
    print ('I RAN!')
