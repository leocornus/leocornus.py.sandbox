have some fun in sorting
========================

Basic sorting technics in Python.
Here is very good how-to:
https://wiki.python.org/moin/HowTo/Sorting

sorting a simple list::

  >>> aList = [4, 5, 2, 1, 3]
  >>> sortedList = sorted(aList)
  >>> print(sortedList)
  [1, 2, 3, 4, 5]

The original list remain the same.::

  >>> print(aList)
  [4, 5, 2, 1, 3]

The sort() function from list object will change he list itself.::

  >>> aList.sort()
  >>> print(aList)
  [1, 2, 3, 4, 5]

Sort complex objects
--------------------

sorted is very handy to sort complex objects.::

  >>> student_tuples = [
  ...         ('john', 'A', 15),
  ...         ('jane', 'B', 12),
  ...         ('dave', 'B', 10),
  ... ]
  >>> sorted(student_tuples, 
  ...        key=lambda student: student[2])   # sort by age
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

we could try list in list.::

  >>> student_tuples = [
  ...         ['john', 'A', 15],
  ...         ['jane', 'B', 12],
  ...         ['dave', 'B', 10]
  ... ]
  >>> sorted(student_tuples, 
  ...        key=lambda student: student[2])   # sort by age
  [['dave', 'B', 10], ['jane', 'B', 12], ['john', 'A', 15]]

sorted is uing ascending as default. the reverse param is for 
descending.::

  >>> sorted(student_tuples, 
  ...        key=lambda student: student[2],   # sort by age
  ...        reverse=True)                     # sort =decending
  [['john', 'A', 15], ['jane', 'B', 12], ['dave', 'B', 10]]
