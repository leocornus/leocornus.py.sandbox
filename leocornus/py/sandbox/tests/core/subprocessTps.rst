Tips for subprocess
===================

import modules and utilities::

  >>> import subprocess
  >>> from subprocess import check_output
  >>> from subprocess import CalledProcessError

check_output and exit status
----------------------------

Each shell command has an exit status (return code).
If the exit status is 0, 
it means the command is executed successfully.
A non-zero exit status normally tells the failure execution.

Test a command which is running successfully::

  >>> output = check_output(["ls", "-la", "/usr"])
  >>> print(output)
  total ...

If It is failed to execute, the CalledProcessError will be expected.
We need set the **stderr** to be **subprocess.STDOUT**.
::

  >>> output = ""
  >>> returncode = 0
  >>> try:
  ...   output = check_output(["ls", "-la", "NONE_EXIT"], 
  ...                         stderr=subprocess.STDOUT)
  ... except CalledProcessError as cpe:
  ...   output = cpe.output
  ...   returncode = cpe.returncode
  >>> print(output)
  ls: ...
  >>> returncode > 0
  True
  >>> print(returncode)
  2

check_output and pipe
---------------------

