Builtin Types
=============

json lib is a convienent way to format a complex data structure.::

  >>> import json

tuple
-----

tuple is more like an array.::

  >>> a = (1, 2)
  >>> print(a[0])
  1
  >>> c, d = a
  >>> print(d)
  2

dump to JSON string::

  >>> print(json.dumps(a))
  [1, 2]

list
----

basic usage around list.::

  >>> l = [2,5]
  >>> m, n = l
  >>> print(n)
  5

we could use index to access the list item.::

  >>> print(l[0])
  2

append will add to the list.::

  >>> l.append([3,9])
  >>> print(l[2])
  [3, 9]

dump to JSON string::

  >>> print(json.dumps(l))
  [2, 5, [3, 9]]

The tuple and list are pretty much the same in JSON world.
But they are completely different object in Python world.

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
