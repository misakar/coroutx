<p align="center">
  <img src="http://ww4.sinaimg.cn/large/a15b4afegw1f6k20fb3p5j205o05ogli" alt="vuepack" width="60">
  <br><br><strong>CoroutX</strong> dead simple python async web framework <br>which use coroutine.
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
```class coroutx.Coroutx()```

    the coroutx object implements a WSGI application and acts as the central object. 

```coroutx.current_app```

    return the current coroutx application
    
```coroutx._request_ctx_hub```

    a coroutine(gevent) local object, store the global request context.

```class coroutx.CoroutxResponse```

    coroutx response class

```class coroutx.CoroutxRequest```

    coroutx request class
    
```function coroutx.route(app, rule)```

    coroutx app route decorator, add url rule.

## coroutx projects

+ [restccnu-grade](https://github.com/Muxi-Studio/restccnu_grade): 华师匣子成绩查询API

## License
MIT, check [LICENSE](https://github.com/neo1218/coroutx/blob/master/LICENSE) for detail.
