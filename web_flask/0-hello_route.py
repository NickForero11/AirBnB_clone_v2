#!/usr/bin/python3
"""Module to make a simple Flask web application.
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
