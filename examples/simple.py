# coding: utf-8

from coroutx import Coroutx, request, route, current_app


app = Coroutx()


headers = {'Status Code': '200'}


@route(app, '/hello/')
@app.tojson
def hello():
    return {
        'url': request.full_path,
        'msg': 'hello coroutx',
        'app': str(current_app)
    }, headers



if __name__ == '__main__':
    app.firing(debug=True)
