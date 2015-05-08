Fabric Git Story
================

Using fabric to manipulate git respository.

Our Goal
--------

Brieflly, we will be able to use Fabric to do the following:

- watch a git repository working folder.
- detect the most recent commit.
- keep a build log for each commit.
- checkout the next commit compare to build log.
- execute test (npm test) for the next commit.
- update build log.

We will use a NPM package on github.com as an example.

Setup
-----

imports::

  >>> import os
  >>> from fabric.operations import local
  >>> from fabric.context_managers import lcd

We will use home folder to test this story.
The **prj_folder** will be the working folder for git repo.
::

  >>> home_folder = os.path.expanduser('~')
  >>> repo_url = 'https://github.com/leocornus/angular-trac-client.git'
  >>> with lcd(home_folder):
  ...     clone = local('git clone %s' % repo_url, True)
  [localhost] local: git clone ...
  >>> prj_folder = os.path.join(home_folder, 'angular-trac-client')

Explore git logs
----------------

Try to find the list of commit id only.
The format option **--format=%h** will make the trick.
::

  >>> with lcd(prj_folder):
  ...     local('git pull', True)
  ...     ids = local('git log --format=%h -10', True)
  [localhost] local: git pull
  'Already up-to-date.'
  [localhost] local: git log ...
  >>> ids = ids.splitlines()
  >>> len(ids)
  10

Execute tests
-------------

Try to execute tests commit by commit.
::
  >>> with lcd(prj_folder):
  ...     checkout = local('git checkout %s' % ids[1], False)
  ...     config = local('git config url."https://".insteadof git://')
  ...     test = local('npm test', False)
  [localhost] local: git checkout ...
  [localhost] local: git config ...
  [localhost] local: npm test

Clean up
--------

remove the projec folder to clean up.
::

  >>> rm = local('rm -rf %s' % prj_folder, False)
  [localhost] local: rm -rf ...
