# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

import time
import random


def app(environ, start_response):
    """Application which cooperatively pauses for a random tenth of second before responding"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))    ]
    time.sleep(random.random() / 10)
    start_response(status, response_headers)
    return iter([data])

