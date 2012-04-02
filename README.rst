=========
cpghstore
=========
:Info: cpghstore is a fast decoder/encoder of the PostgreSQL hstore
       data type (http://www.postgresql.org/docs/9.0/static/hstore.html).
:Author: Robert Kajic (http://github.com/kajic)

About
=====
cpghstore is written in C and is meant to be a faster alternative to
`pghstore <http://pypi.python.org/pypi/pghstore>`_. Run ``python setup.py
test -s benchmark`` to see how it performs (requires pghstore to be installed if
you want comparisons to be shown).

Installation
============
Download the
source from `GitHub <http://github.com/kajic/cpghstore>`_ and run ``python
setup.py install``.

Usage
=====
Decode and encode hstore string::

    >>> import cpghstore
    >>> # decode
    >>> d = cpghstore.loads('"name"=>"Norge/Noreg"')
    >>> d
    {'name': 'Norge/Noreg'}
    >>> # encode
    >>> s = cpghstore.dumps(d)
    >>> s
    '"name"=>"Norge/Noreg"'

Tests
=====
To run the test suite, run ``python setup.py test``.

Benchmark
=========
Run ``python setup.py test -s benchmark`` to see how it performs (requires
pghstore to be installed if you want comparisons to be shown).

Limitations
===========
Supports only str strings (i.e. not unicode string).
Can only decode (loads) string values, i.e. "key"=>"123" is supported but
"key"=>123 is not.