# coding: utf-8
"""
    hub.py
    ``````

    realize a hub greenlets :_request_ctx_hub: for request context
    greenlet switching.

    :copyright: (c) 2016 by neo1218.
    :license: MIT, see LICENSE for more details.
"""

# from gevent.wsgi import WSGIServer
from gevent.local import local
from werkzeug.local import LocalProxy


_request_ctx_hub = local()


request = LocalProxy(lambda: _request_ctx_hub.request)
current_app = LocalProxy(lambda: _request_ctx_hub.app)
