from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello world'


@app.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
