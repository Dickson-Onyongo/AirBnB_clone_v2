#!/usr/bin/python3
"""Script that starts a Flask web application on host 0.0.0.0
and port 5000.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """Returns a greeting message "Hello HBNB" """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def HBNB_page():
    """Returns a short message "HBNB" """
    return"HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """Display “C ”followed by the value of the text variable"""
    formated_text = text.replace('_', ' ')
    return f"C {formated_text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Display “Python” followed by the value of the text variable"""
    formated_text = text.replace('_', ' ')
    return f"Python {formated_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
