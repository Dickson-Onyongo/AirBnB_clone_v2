#!/usr/bin/python3
"""Script that starts flask web application on port 5000."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns A greeting message "Hello HBNB!" """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
