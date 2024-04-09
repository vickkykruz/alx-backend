#!/usr/bin/env python3
""" This is a module run the index page on task 0 """


import secrets
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ This is a function that render index page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
