"""Provides main routes"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    """Display homepage"""
    return 'Hello world'


@app.route('/hello/<name>')
def hello(name):
    """Display hello with given url parameter"""
    return 'Hello ' + name


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
