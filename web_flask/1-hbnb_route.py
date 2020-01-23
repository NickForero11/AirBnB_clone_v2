#!/usr/bin/python3
"""Module to make a simple Flask web application with multiple routes.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root_page():
    """Helper function to serve a message on the '/' route.

    Take in account that this function will be triggered
    with or without trailing slashes ('0.0.0.0:5000' or '0.0.0.0:5000/').

    Decorators:
        app.route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Helper function to serve a message on the '/hbnb' route.

    Take in account that this function will be triggered
    with or without trailing slashes, it means that it will be available at:
    ('0.0.0.0:5000/hbnb' or '0.0.0.0:5000/hbnb/').

    Decorators:
        app.route
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
