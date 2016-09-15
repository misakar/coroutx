# coding: utf-8

import time
from coroutx import Coroutx, request, route, current_app


app = Coroutx()


@route(app, '/hello/')
@app.tojson
def hello():
    return 'hello coroutx'

@route(app, '/timeout/')
@app.tojson
def timeout():
    # time.sleep(60)
    time.sleep(6)
    return "timeout"


if __name__ == '__main__':
    app.firing(debug=True)
