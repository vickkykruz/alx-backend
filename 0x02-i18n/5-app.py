#!/usr/bin/env python3
""" This is a module that c-reating a user login system is outside the scope of
this project
"""


from flask import Flask, request, render_template, g
import flask_babel


app = Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    """ This is a Config class """

    LANGUAGES = ["en", "fr"]  # Define supported languages
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """ This is a function that return the user id """
    return users.get(user_id)


@app.before_request
def before_request():
    """ This is a function that check if the user exist and fetches the
    details """

    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """ This is a function that return the accept language """
    if g.user:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ This is a function that return the index page """

    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
