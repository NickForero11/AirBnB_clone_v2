#!/usr/bin/python3
"""Module to make a simple Flask web application with multiple routes and
variable rules with default parameters.
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


@app.route('/c/<text>', strict_slashes=False)
def c_message(text):
    """Helper function to serve a message on the '/c' route and
    the served message is “C ” followed by the value of the text variable.


    Take in account that this function will be triggered
    with or without trailing slashes, it means that it will be available at:
    ('0.0.0.0:5000/c/<text>' or '0.0.0.0:5000/c/<text>/').

    Arguments:
        text (str): A string that contains the message that will be printed,
                    Note: the underscore _ symbols are replaced with a space.

    Decorators:
        app.route
    """
    message = text.replace('_', ' ')
    response = 'C {}'.format(message)
    return response


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_message(text):
    """Helper function to serve a message on the '/python' route and
    the served message is “Python ” followed by the value of the text variable.


    Take in account that this function will be triggered
    with or without trailing slashes, it means that it will be available at:
    '0.0.0.0:5000/python/<text>'    or    '0.0.0.0:5000/python/<text>/' or
    '0.0.0.0:5000/python/'          or    '0.0.0.0:5000/python'

    Arguments:
        text (str): A string that contains the message that will be printed,
                    Note: the underscore _ symbols are replaced with a space.

    Decorators:
        app.route
    """
    message = text.replace('_', ' ')
    response = 'Python {}'.format(message)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
