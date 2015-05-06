Get Started with development
============================

Simple example with eve_sqlalchemy module and sqlite database.

Dependences:

- sqlalchemy
- eve_sqlalchemy
- eve
- flask

Import basic class from module **sqlalchemy**.
::

  >>> from sqlalchemy import Column
  >>> from sqlalchemy import String
  >>> from sqlalchemy import Integer
  >>> from sqlalchemy.orm import column_property
  >>> from sqlalchemy.ext.declarative import declarative_base

import the Eve_SQLAlchemy module.
::

  >>> from eve_sqlalchemy import SQL
  >>> from eve_sqlalchemy.validation import ValidatorSQL
  >>> from eve_sqlalchemy.decorators import registerSchema

import the Eve framework.
:: 

  >>> from eve import Eve

Get started from a simple sqlalchemy class.
::

  >>> Base = declarative_base()
  >>> class People(Base):
  ...     __tablename__ = 'people'
  ...     id = Column(Integer, primary_key=True, autoincrement=True)
  ...     first_name = Column(String(120))
  ...     last_name = Column(String(120))
  ...     full_name = column_property(first_name + " " + last_name)
  ... 
  ...     @classmethod
  ...     def from_tuple(cls, data):
  ...         """Helper method to populate data"""
  ...         return cls(first_name=data[0], last_name=data[1])

Register the class.
::

  >>> s = registerSchema('people')(People)

Now get ready the settings for Eve.
::

  >>> settings = {
  ...     'DEBUG': True,
  ...     'SQLALCHEMY_DATABASE_URI': 'sqlite://',
  ...     'DOMAIN': {
  ...         'people': People._eve_schema['people'],
  ...         }
  ... }

Construct the Eve app.
::

  >>> app = Eve(auth=None, settings=settings, 
  ...           validator=ValidatorSQL, data=SQL)

