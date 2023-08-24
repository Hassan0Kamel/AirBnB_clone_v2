#!/usr/bin/python3
"""0x1. HBNB
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
    """Test th.
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
