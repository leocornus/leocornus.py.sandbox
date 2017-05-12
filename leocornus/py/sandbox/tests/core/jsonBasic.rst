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

Now, we have a object. Let's try the encode it to string.
In some case, we also call it stringify.::

  >>> stringAgain = json.dumps(jsonObj)
  >>> print(stringAgain)
  {"a": "one", "b": "two"}

Here is how to make it pretty.::

  >>> print(json.dumps(jsonObj, sort_keys=True, indent=2))
  {
    "a": "one",
    "b": "two"
  }
