# coding: utf-8

from coroutx import Coroutx, request, route, current_app


app = Coroutx()


@route(app, '/hello/')
@app.tojson
def hello():
    return 'hello coroutx'


if __name__ == '__main__':
    app.firing(debug=True)
