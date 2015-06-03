Gunicorn
--------

.. image::
    https://secure.travis-ci.org/benoitc/gunicorn.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/benoitc/gunicorn

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn_ project. The Gunicorn server is broadly
compatible with various web frameworks, simply implemented, light on server
resource usage, and fairly speedy.

Feel free to join us in `#gunicorn`_ on Freenode_.

Documentation
-------------

The documentation is hosted at http://docs.gunicorn.org.

Installation
------------

Gunicorn requires **Python 2.x >= 2.6** or **Python 3.x >= 3.2**.

Install from PyPI::

    $ pip install gunicorn


Usage
-----

Basic usage::

    $ gunicorn [OPTIONS] APP_MODULE

Where ``APP_MODULE`` is of the pattern ``$(MODULE_NAME):$(VARIABLE_NAME)``. The
module name can be a full dotted path. The variable name refers to a WSGI
callable that should be found in the specified module.

Example with test app::

    $ cd examples
    $ gunicorn --workers=2 test:app

Introspection
-------------

This section is specific to the patched gunicorn version Zuisite uses (0.13.3.prezi2).
In case a SIGILL signal is sent to a worker process it will dump out its open
requests and their stack traces to a specific file under /tmp. If the signal is
sent to the master it broadcasts it to every worker. E.g.::

    [app10.us:~] $ cat /var/run/zuisiteplacement.pid
    14080
    [app10.us:~] $ kill -SIGILL 14080
    [app10.us:~] $ ls /tmp/gunicornsigill_20140623190857_*
    ...
    /tmp/gunicornsigill_20140623190857_10689
    ...

For version 18.0.prezi1 the temporary directory is generated randomly by default. If
one wants to specify where the state dumps should go than the worker-tmp-dir config
argument should be used, e.g.::

    --worker-tmp-dir=/var/tmp

Integration
-----------

We also provide integration for both Django and Paster applications.

Django
++++++

gunicorn just needs to be called with a the location of a WSGI
application object.:

    gunicorn [OPTIONS] APP_MODULE

Where APP_MODULE is of the pattern MODULE_NAME:VARIABLE_NAME. The module
name should be a full dotted path. The variable name refers to a WSGI
callable that should be found in the specified module.

So for a typical Django project, invoking gunicorn would look like:

    gunicorn myproject.wsgi:application

(This requires that your project be on the Python path; the simplest way
to ensure that is to run this command from the same directory as your
manage.py file.)

You can use the
`--env <http://docs.gunicorn.org/en/latest/settings.html#raw-env>`_ option
to set the path to load the settings. In case you need it you can also
add your application path to PYTHONPATH using the
`--pythonpath <http://docs.gunicorn.org/en/latest/settings.html#pythonpath>`_
option.

Paste
+++++

If you are a user/developer of a paste-compatible framework/app (as
Pyramid, Pylons and Turbogears) you can use the gunicorn
`--paste <http://docs.gunicorn.org/en/latest/settings.html#paste>`_ option
to run your application.

For example:

    gunicorn --paste development.ini -b :8080 --chdir /path/to/project

It is all here. No configuration files nor additional python modules to
write !!


License
-------

Gunicorn is released under the MIT License. See the LICENSE_ file for more
details.

.. _Unicorn: http://unicorn.bogomips.org/
.. _`#gunicorn`: http://webchat.freenode.net/?channels=gunicorn
.. _Freenode: http://freenode.net
.. _LICENSE: http://github.com/benoitc/gunicorn/blob/master/LICENSE
