#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_main():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def profile(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def profile_python(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n is a number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display n is a number"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
