Python Math basic
=================

The first challendge from Google foo.bar.

define the function::

  >>> def answer(area):
  ...  
  ...     # import libs.
  ...     import math
  ... 
  ...     # find out the integer square root of the given area.
  ...     intSqrt = int(math.sqrt(area))
  ...     # caculate the remain area.
  ...     remainArea = area - intSqrt * intSqrt
  ...     # get ready the return number.
  ...     ret = []
  ...     # add the biggest section
  ...     ret.append(intSqrt * intSqrt)
  ...     # handle the remaining area.
  ...     if remainArea > 4:
  ...         # the remaining area is big enough for another square root
  ...         ret = ret + answer(remainArea)
  ...     else:
  ...         # appending 1 for the remaining
  ...         for i in range(0, remainArea):
  ...             ret.append(1)
  ...
  ...     return ret

verify

  >>> print answer(12)
  [9, 1, 1, 1]
