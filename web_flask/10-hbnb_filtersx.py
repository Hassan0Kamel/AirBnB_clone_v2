#!/usr/bin/python3
"""0x0filters
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def states_list_teardown(self):
    """ Ensurelosed after serving.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Requestlate served to '/hbnb_filters'.
    """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State),
                           cites=storage.all(City),
                           amenities=storage.all(Amenity))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
