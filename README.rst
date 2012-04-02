=========
cpghstore
=========
:Info: cpghstore is a fast decoder/encoder of the PostgreSQL hstore
       data type (http://www.postgresql.org/docs/9.0/static/hstore.html).
:Author: Robert Kajic (http://github.com/kajic)

About
=====
cpghstore is written in C and is meant to be a faster (up to ~130x faster
decoding, up to ~60x faster encoding) alternative to
`pghstore <http://pypi.python.org/pypi/pghstore>`_. Run ``python setup.py
benchmark`` to see how it performs (requires pghstore to be installed if you
want comparisons to be shown).

Installation
============
Download the
source from `GitHub <http://github.com/kajic/cpghstore>`_ and run ``python
setup.py install``.

Tests
=====
To run the test suite, run ``python setup.py test``.

Benchmark
=========
Run ``python setup.py benchmark`` to see how it performs (requires pghstore to 
be installed if you want comparisons to be shown).

Limitations
===========
Can only decode (loads) string values, i.e. "key"=>"123" is supported but
"key"=>123 is not.