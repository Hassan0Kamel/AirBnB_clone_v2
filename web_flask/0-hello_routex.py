#!/usr/bin/python3
"""0x0ello Flask!
"""
from flask import Flask
from os import environ

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.route('/', strict_slashes=False)
def hello():
    """Test meost port 5000
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
