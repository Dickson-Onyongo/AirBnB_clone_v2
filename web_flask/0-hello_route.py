#!/usr/bin/python3
from flask import Flask
"""
script that starts flask web application on port 500.

"""
app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello():
    return "Hello HBNB!"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
