#!/usr/bin/env python3
""" This is a module that Change your get_locale function to use a user’s
preferred local if it is supported.
"""


from flask import Flask, render_template, request, g
import flask_babel


app = Flask(__name__)
babel = flask_babel.Babel(app)


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ This is a config class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user(user_id):
    """ This function return the user_id """

    return users.get(user_id)


@app.before_request
def before_request():
    """ This function return the request details of the user """

    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """ This function process the location of the user """

    # Check if locale is specified in URL parameters
    if 'locale' in request.args and request.args[
            'locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    # Check if user is logged in and their preferred locale is supported
    elif g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    # Use the request header to determine the preferred locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ This function render the index template """

    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
