#!/usr/bin/python3
"""Using flask framework 2
"""

from flask import Flask
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hello():
    return "HBNB"


if __name__ == '__main__':
    app.run()
