#!/usr/bin/python3
"""0x0B is alive!
"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User


app = Flask(__name__)
environ['FLASK_ENV'] = 'development'


@app.teardown_appcontext
def states_list_teardown(self):
    """ Ensuresed after serving.
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Requeststhe HTML template served to '/hbnb_filters'.
    """
    return render_template('100-hbnb.html',
                           states=storage.all(State),
                           cites=storage.all(City),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place),
                           users=storage.all(User))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
