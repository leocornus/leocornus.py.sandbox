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

You should be able to remove more then one characters.::

  >>> b = '<><><><>abc<><><><>   '
  >>> b.lstrip('<>')
  'abc<><><><>   '
