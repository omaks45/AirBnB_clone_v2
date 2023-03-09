#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a given string"""
    return ("Hello HBNB!")

@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():
    """Return a given string"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
