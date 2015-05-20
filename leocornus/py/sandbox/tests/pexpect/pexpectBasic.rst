Basic (core) Pexpect
====================

Explore the core components of pexpect_.
::

  >>> import pexpect
  >>> import os
  >>> from os import chdir
  >>> from os import path

.. contents:: Table of Contents
   :depth: 5

Basic run
---------

What's the output for the **run** method?
::

  >>> output = pexpect.run('ls -la')
  >>> print(output)
  total ...

Basic spawn
-----------

The class **spawn** is the main class for pexpect_.
::

  >>> from pexpect import spawn

run the command **ls -la** by using the spawn class.
::

  >>> http_server = spawn('ls -la')
  >>> print(http_server.before)
  None
  >>> # expect returns the index of the pattern in the list.
  >>> index = http_server.expect(pexpect.EOF)
  >>> print(http_server.before)
  total ... 
  >>> http_server.close()
  >>> # exist status is 0 tells the command execute successfully.
  >>> print(http_server.exitstatus)
  0

testing the return code:

:0:
  executed successfully

:none-zero:
  failed for error

::

  >>> none_exist =spawn('ls -la NONE_exist')
  >>> index = none_exist.expect(pexpect.EOF)
  >>> print(none_exist.before)
  /...NONE_exist: No such file or directory
  >>> none_exist.close()
  >>> none_exist.exitstatus > 0
  True

Handle nodejs Project
---------------------


The **logfile** in **spawn** class is like the **stdout** for subprocess.
If **logfile** is none (which is default), all output will be stream
**before** variable.

prepare some log files
~~~~~~~~~~~~~~~~~~~~~~

get ready the testing folder for log files.
::

  >>> home_folder = path.expanduser("~")
  >>> test_folder = path.join(home_folder, 'pexpect')
  >>> os.mkdir(test_folder)
  >>> path.exists(test_folder)
  True

create log files for buildlog.
::

  >>> build_log = path.join(test_folder, '.buildlog')
  >>> npm_log = path.join(test_folder, '.npmlog')
  >>> output = pexpect.run('touch %s' % build_log)
  >>> output = pexpect.run('touch %s' % npm_log)
  >>> path.exists(build_log)
  True
  >>> build_log = open(build_log, 'w+r')
  >>> path.exists(npm_log)
  True
  >>> npm_log = open(npm_log, 'w+r')

Clone a npm project from github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

using the leocorns-ci-projects
::

  >>> repo_url = 'https://github.com/leocornus/leocornus-ci-projects.git'

Start the http_server, CTRL-C tells the the http_server is started.
::

  >>> chdir(test_folder)
  >>> clone = pexpect.run('git clone --depth=10 %s' % repo_url)
  >>> phonecat_folder = path.join(test_folder, 
  ...                             'leocornus-ci-projects',
  ...                             'projects', 'phonecat')
  >>> chdir(phonecat_folder)
  >>> # set up git to use https
  >>> https = pexpect.run('git config url."https://".insteadof git://')
  >>> http_server = spawn('npm start', logfile=npm_log, timeout=300)
  >>> index = http_server.expect('CTRL-C')
  >>> # try use the send method.
  >>> #http_server.send('aaa')

execute the e2e test cases.
::

  >>> protractor = spawn('npm run protractor', 
  ...                    logfile=build_log,
  ...                    timeout=300)
  >>> index = protractor.expect(pexpect.EOF)
  >>> protractor.close()

show the e2e test result.
::

  >>> print(build_log.read())
  >>> print(protractor.before)

shutdown http_server, force close. sendcontrol('c')
we will need the before and after expect match.
::

  >>> #http_server.close(True)
  >>> r = http_server.sendcontrol('c')
  >>> print(npm_log.read())

clean up
--------

Just need remove the test folder.
::

  >>> os.chdir(home_folder)
  >>> output = pexpect.run('rm -rf %s' % test_folder)

.. _pexpect: https://github.com/pexpect/pexpect
