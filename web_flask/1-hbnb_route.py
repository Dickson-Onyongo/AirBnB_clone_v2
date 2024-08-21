#!/usr/bin/python3
"""Script that starts a Flask web application on host 0.0.0.0
and port 500.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """Returns a greeting message "Hello HBNB" """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Returns a short message "HBNB" """
    return"HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
