#!/usr/bin/env python3
""" This is a module run the index page on task 0 """


import secrets
from flask import Flask, render_template


def create_application():
    """ This is a function that create the application """

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)


    @app.route("/")
    def index_page():
        """ This is a function that render the index template """
        return render_template("index.html")

    return app


if __name__ == "__main__":
    # call the function
    app = create_application()

    app.run(host="0.0.0.0", port="5000", debug=True)
