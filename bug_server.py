from random import choice
from string import ascii_uppercase
import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/test/')
def test():
    return "It Worked! " + ''.join(choice(ascii_uppercase) for i in range(5))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
