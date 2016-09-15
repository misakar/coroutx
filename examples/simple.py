# coding: utf-8

import gevent
from coroutx import Coroutx, request, route, current_app, url_map


app = Coroutx()

headers = {'Status Code': '200'}

session = {}  # simply a global dict

@route(app, '/hello/')
@app.tojson
def hello():
    session['username'] = request.args.get('username')
    return {
        'url': request.full_path,
        'msg': 'hello coroutx',
        'app': str(current_app)
    }, headers


@route(app, '/hello2/')
@app.tojson
def hello2():
    return {
        'url': request.full_path,
        'msg': 'hello {}'.format(session.get('username')),
        'app': str(current_app)
    }, headers


#url_map.yo(app, rule='/hello/', methods=['GET'], handler=hello)
#url_map.yo(app, rule='/hello/', methods=['GET'], handler=hello2)

app.firing(host='localhost', port=8090)
