Python Basic
============

Get to know Python language in basic.

.. contents:: Table of Contents
   :depth: 5

Basic Operation
---------------

Obervious things::

  >>> 1 + 3
  4
  >>> a = [1, 2, 3]
  >>> sum(a)
  6

Basic os Module
---------------

  >>> import os

How to find current user's home folder::

  >>> homeFolder = os.path.expanduser('~')

Create a folder::

  >>> testFolder = os.path.join(homeFolder, 'testtmp')
  >>> os.path.exists(testFolder)
  False
  >>> os.mkdir(testFolder)
  >>> os.path.exists(testFolder)
  True

Change current direct director::

  >>> os.chdir(testFolder)

Get current directory::

  >>> print(os.getcwd()) # doctest: +ELLIPSIS
  /home/.../testtmp

To avoid get errors lik this::

  shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory

We need change current directory back to default directory,
which is the home directory.::

  >>> os.chdir(homeFolder)

Basic shutil Module
-------------------

  >>> import shutil

Remove a whole folder, including files and subfolders in it.
This is typically helpful for testing script::

  >>> shutil.rmtree(testFolder)

Basic String Operator
---------------------

Try the splitlines::

  >>> lines = """line one
  ... line two
  ... line three
  ... """
  >>> lines.splitlines()
  ['line one', 'line two', 'line three']

Check a string ends with something::

  >>> aName = 'someting.ends'
  >>> aName.endswith('.ends')
  True
