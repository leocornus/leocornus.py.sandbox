Learn ansi2html by writing test cases
=====================================

First of all we will test does ansi2html is load properly?
We using buildout to install ansi2html egg.
Load the core module to execute some bash commands.
::

  >>> from subprocess import check_output

The simplest test to make sure we hve ansi2html installed
::

  >>> from ansi2html import Ansi2HTMLConverter
  >>> conv = Ansi2HTMLConverter()
  >>> ansi = check_output(["ls", "-ls", "--color", "/usr"])
  >>> html = conv.convert(ansi);
  >>> print(html)

Write to file to check more.
::

  >>> file_name = '/tmp/ansi.html'
  >>> operator = open(file_name, 'w')
  >>> try:
  ...     operator.write(html)
  ... finally:
  ...     operator.close()
