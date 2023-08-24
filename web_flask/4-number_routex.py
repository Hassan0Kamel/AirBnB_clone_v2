#!/usr/bin/python3
"""0x0it a number?
"""
from flask import Flask
from os import environ

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.route('/', strict_slashes=False)
def index():
    """Test
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Testh.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_subpath(text):
    """Test me subpaths into message text.
    """
    return ' '.join(['C', text.replace('_', ' ')])


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_subpath(text='is cool'):
    """Test meverting subpaths into message text, with
    a defaing.
    """
    return ' '.join(['Python', text.replace('_', ' ')])


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Test met integer.
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
