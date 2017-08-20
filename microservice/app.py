# -*- coding: utf-8 -*-
"""
App runner
"""
import falcon


app = falcon.API()


if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
