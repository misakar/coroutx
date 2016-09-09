<p align="center">
  <br><strong>CoroutX</strong> dead simple python async web framework <br>based on coroutine.
</p>

## Benchmark


## Example

    # coding: utf-8

    import gevent
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

## API
class coroutx.Coroutx() <br/>

    the coroutx object implements a WSGI application and acts as the central object. 

coroutx.current_app <br/>

    return the current coroutx application
    
coroutx._request_ctx_hub <br/>

    a coroutine(gevent) local object, store the global request context.

class coroutx.CoroutxResponse <br/>

    coroutx response class

class coroutx.CoroutxRequest <br/>

    coroutx request class
    
function coroutx.route(app, rule) <br/>

    coroutx app route decorator, add url rule.

## coroutx projects

+ [restccnu-grade](https://github.com/Muxi-Studio/restccnu_grade): 华师匣子成绩查询API

## License
MIT, check [LICENSE](https://github.com/neo1218/coroutx/blob/master/LICENSE) for detail.
