<p align="center">
  <br><strong>CoroutX</strong> dead simple python async web framework <br>based on coroutine.
</p>

## Benchmark
```(coroutx vs flask)``` <br/>
Results bellow were received with MacBook Air, CPU: 1.6 GHz i5, MEM: 4GB, OSX 10.10.4. I've used a [siege](https://github.com/JoeDog/siege) utility with params: <br/>

    $ siege -c 200 -r 10 [url]

The tests were running from gevent pywsgi server <br/>
+ [flask]() <br/>

code see [benchmark]() <br/>
Results: <br/>
coroutx:

    Transactions:		        1000 hits
    Availability:		      100.00 %
    Elapsed time:		        3.34 secs
    Data transferred:	        0.01 MB
    Response time:		        0.07 secs
    Transaction rate:	      299.40 trans/sec
    Throughput:		        0.00 MB/sec
    Concurrency:		       20.72
    Successful transactions:        1000
    Failed transactions:	           0
    Longest transaction:	        0.29
    Shortest transaction:	        0.00

flask:

    Transactions:		        1000 hits
    Availability:		      100.00 %
    Elapsed time:		        3.32 secs
    Data transferred:	        0.01 MB
    Response time:		        0.04 secs
    Transaction rate:	      301.20 trans/sec
    Throughput:		        0.00 MB/sec
    Concurrency:		       12.05
    Successful transactions:        1000
    Failed transactions:	           0
    Longest transaction:	        0.18
    Shortest transaction:	        0.00

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
