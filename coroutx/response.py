# coding: utf-8
"""
    resp.py
    ```````

    coroutx response class
"""

from werkzeug.wrappers import Response


class CoroutxResponse(Response):
    """
    :class CoroutxResponse:
        the response object used by default in Coroutx,
        but set default content-type as 'application/json'
    """
    # content_type = 'application/json'
    pass
