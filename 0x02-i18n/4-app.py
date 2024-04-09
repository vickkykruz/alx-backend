#!/usr/bin/env python3
""" This is a module run the index page on task 0 """


from flask import Flask, render_template, request
import flask_babel


app = Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    """ This is a Config class that handle the babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ This is a function that return the locale via request """
    # Check if 'locale' parameter is in the request URL
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ This is a function that render index page """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
