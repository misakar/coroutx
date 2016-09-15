# coding: utf-8
"""
    route.py
    ````````

    coroutx route decorator.

    :copyright: (c) 2016 by neo1218.
    :license: MIT, see LICENSE for more details.
"""

import functools
from werkzeug.routing import Rule, Map


class CoroutxRuleMap(Map):
    """
    app.url_map.yo(app, path='/ping/', methods=['GET'], handler=yo)
    """
    def yo(self, app, rule, methods, handler):
        endpoint = handler.__name__
        app.url_map.add(Rule(
            rule=rule, methods=methods, endpoint=endpoint
        ))
        app.route_functions[endpoint] = handler


def route(app, rule, **options):
    """
    :decorator function: route
        add url rule, map url rule 2 route functions

    :param app: the coroutx app
    :param rule: the url rule
    """
    def decorator(f):
        if 'endpoint' not in options:
            options['endpoint'] = f.__name__
        app.url_map.add(Rule(rule, **options))        # add url rule
        app.route_functions[options['endpoint']] = f  # {'endpoint': func}
        return f
    return decorator
