Python json in basic
====================

Some basic ideas for using json in Python application.

In Python, json is a built-in lib, just simply import it::

  >>> import json
  >>> print(json)
  <module 'json' from...>

Let's get started with a json string. The string has to be 
surrounded by single quote.::

  >>> jsonString = '{"a":"one", "b":"two"}'
  >>> print(jsonString)
  {"a":"one", "b":"two"}

The function **loads** will parse or decode json string::

  >>> jsonObj = json.loads(jsonString)
  >>> print(jsonObj)
  {u'a': u'one', u'b': u'two'}
