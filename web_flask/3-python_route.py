#!/usr/bin/python3
""" Starts a Flask web app
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        /python/(<text>): display “Python ”,
        followed by the value of the text variable
        The default value of text is “is cool”
        (replace underscore _ symbols with a space)
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return "Python {}".format(escape(text))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
