Test cases for string functions
===============================

This file is try to host a list of functions to process string.

lstrip
------

This function will remove the leading characters.

By default, lstrip will remove all leading white spaces.::

  >>> a = '   abcd   '
  >>> a.lstrip()
  'abcd   '

You could set the character you want to remove.::

  >>> a = '>>>>abcd >>>a>>>'
  >>> a.lstrip('>')
  'abcd >>>a>>>'

You should be able to remove more than one characters.::

  >>> b = '<><><><>abc<><><><>   '
  >>> b.lstrip('<>')
  'abc<><><><>   '

In multi-characters case, it could be characters mixed with
white space and other characters.::

  >>> a = '  <>this is the real content'
  >>> a.lstrip('  <>')
  'this is the real content'

Remove multi lines.::

  >>> a = '  <>Line one\n  <>Line Two'
  >>> a
  '  <>Line one\n  <>Line Two'
  >>> print(a)
    <>Line one
    <>Line Two
  >>> b = a.lstrip('  <>')
  >>> print(b)
  Line one
    <>Line Two
