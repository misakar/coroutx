# coding: utf-8

import time
from flask import Flask


app = Flask(__name__)


@app.route('/hello/')
def hello():
    return 'hello flask'

@app.route('/timeout/')
def timeout():
    # time.sleep(60)
    time.sleep(6)
    return "timeout"


if __name__ == '__main__':
    app.run(debug=True)
