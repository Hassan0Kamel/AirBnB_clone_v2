#!/usr/bin/python3
"""0x0 or even?
"""
from flask import Flask, render_template
from os import environ

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.route('/', strict_slashes=False)
def index():
    """Test meth
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Test me
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_subpath(text):
    """Test mting subpaths into message text.
    """
    return ' '.join(['C', text.replace('_', ' ')])


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_subpath(text='is cool'):
    """Test mnverting subpaths into message text, with
    a default string.
    """
    return ' '.join(['Python', text.replace('_', ' ')])


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Test methonly if subpath is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Test metpath, only if subpath is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Test methath, only if subpath is an integer.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
