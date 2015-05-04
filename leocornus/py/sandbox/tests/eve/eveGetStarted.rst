Get started with eve
====================

Get ready a mini setting::

  >>> mini_settings = {
  ...   'DOMAIN' : {'people' : {}}
  ... }

::

  >>> from eve import Eve
  >>> from eve_sqlalchemy import SQL
  >>> app = Eve(settings=mini_settings, data=SQL)
  >>> #app.run()

