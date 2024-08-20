#!/usr/bin/python3

from flask import Flask

"""
Script that starts a Flask web application on host 0.0.0.0
and port 500.

"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    return "Hello HBNB"


"""
Returns a greeting message.

Returns
------
str
    Return: returns a greeting message, "Hello HBNB"

"""


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return"HBNB"


"""
Returns a short message.

Returns
------
str
    Return: returns a  message, "HBNB"

"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
