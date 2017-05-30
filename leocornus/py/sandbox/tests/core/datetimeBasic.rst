datetime basic ideas in Python
==============================

Python has the builtin lib datetime::

  >>> import datetime

The method strptime will parse a date::

  >>> startDate = '2017-04-01'
  >>> start = datetime.datetime.strptime(startDate, '%Y-%m-%d')
  >>> print(start.date())
  2017-04-01

Let try to get a range of date::

  >>> endDate = '2017-05-25'
  >>> end = datetime.datetime.strptime(endDate, '%Y-%m-%d')

set up the step using timedelta method::

  >>> step = datetime.timedelta(days=1)
  >>> dates = []

get the time range inclusively::

  >>> while start <= end:
  ...     dates.append(start.date())
  ...     start += step
  >>> print(dates[0])
  2017-04-01
  >>> print(dates[54])
  2017-05-25

check the total dates::

  >>> len(dates)
  55
