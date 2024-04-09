#!/usr/bin/env python3
""" This is a module run the index page on task 0 """


from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


# Set up Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'French'
}


# Routes
@app.route('/')
def home():
    return render_template('3-index.html')


# Jinja2 filters
@babel.localeselector
def get_locale():
    return 'fr'


if __name__ == '__main__':
    app.run(debug=True)
