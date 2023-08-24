#!/usr/bin/python3
"""0x04mber template
"""
from flask import Flask, render_template
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
    """Test m.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_subpath(text):
    """Test meonverting subpaths into message text.
    """
    return ' '.join(['C', text.replace('_', ' ')])


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_subpath(text='is cool'):
    """Testlt string.
    """
    return ' '.join(['Python', text.replace('_', ' ')])


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Test only if subpath is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Testate/` path, only if subpath is an integer.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
