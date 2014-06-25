import os
import sys

from setuptools import setup

if sys.version_info < (2, 7):
    tests_require = ['unittest2']
else:
    tests_require = []


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-KVSession',
    version='0.5dev',
    url='https://github.com/mbr/flask-kvsession',
    license='MIT',
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    description='Transparent server-side session support for flask',
    long_description=read('README.rst'),
    py_modules=['flask_kvsession'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.8', 'simplekv>=0.9', 'werkzeug', 'itsdangerous>=0.20', 'six',
    ],
)
