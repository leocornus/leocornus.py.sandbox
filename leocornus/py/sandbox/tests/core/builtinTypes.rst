Builtin Types
=============

tuple
-----

::

  >>> a = (1, 2)
  >>> print(a[0])
  1
  >>> c, d = a
  >>> print(d)
  2

list
----

::

  >>> l = [2,5]
  >>> m, n = l
  >>> print(n)
  5

string
------

How to ::

  >>> a = 'abc'
  >>> b = 'cde'
  >>> a + b
  'abccde'
  >>> b + a
  'cdeabc'

The behavour around multi lines::

  >>> a = 'abc\ncde'
  >>> print(a)
  abc
  cde
