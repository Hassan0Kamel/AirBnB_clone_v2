#!/usr/bin/python3
"""0x0on is cool!
"""
from flask import Flask
from os import environ

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.route('/', strict_slashes=False)
def index():
    """Tes.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Test meth
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_subpath(text):
    """Test methnverting subpaths into message text.
    """
    return ' '.join(['C', text.replace('_', ' ')])


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_subpath(text='is cool'):
    """Test meth, converting subpaths into message text.
    """
    return ' '.join(['Python', text.replace('_', ' ')])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
