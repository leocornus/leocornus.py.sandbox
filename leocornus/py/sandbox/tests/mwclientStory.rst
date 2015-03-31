Story about mwclient
====================

This is a basic learning story about mwclient_.

.. contents::
   :depth: 5

Query Wikipedia
---------------

This is the basic usage of mwclient_. 
The following testing is mainly based on mwclient_ tutorial.

Try to connect to wikipedia site, the api.php is located at 
path **/w/**. That is also the default path.::

  >>> import mwclient
  >>> site = mwclient.Site('en.wikipedia.org')
  >>> site
  <Site object 'en.wikipedia.org/w/'>

Try to get the **Special:Version** page as a quick test.
The special page should have NO text::

  >>> version = site.Pages['Special:Version']
  >>> version.text()
  u''

Get categories of a page

Get revisions of a page.

Using .mwrc for configuration
-----------------------------

Need os module to access file system.

  >>> import os

Read from ~/.mwrc file. 
The **~/.mwrc** file should have the following format::

  [mwclient]
  host = domain.of.wiki.site
  path = /wiki/
  username = username
  password = password

Login, Create, and Replace Wiki Page
------------------------------------

If the file is not exist, we will skip the whole section.
::

  >>> homeFolder = os.path.expanduser('~')
  >>> mwrc = os.path.join(homeFolder, '.mwrc')
  >>> if os.path.exists(mwrc):
  ...     # using ConfigParser module.
  ...     import ConfigParser
  ...     rc = ConfigParser.ConfigParser()
  ...     # read method will return the filename in a list.
  ...     filename = rc.read(mwrc)
  ...     host = rc.get('mwclient', 'host')
  ...     path = rc.get('mwclient', 'path')
  ...     username = rc.get('mwclient', 'username')
  ...     password = rc.get('mwclient', 'password')
  ...     site = mwclient.Site(host, path=path)
  ...     print(site) # doctest: +ELLIPSIS
  ...     site.login(username, password)
  ...     testPage = site.Pages['Testing Page']
  ...     text = testPage.edit()
  ...     text = """Tesing page! 
  ... nothing for now
  ... 
  ... maybe something new in the future"""
  ...     text = text + '[[Category: Testing]]'
  ...     ret = testPage.save(text, summary="this is a quick test")
  ...     print(ret['title'])
  ...     print(ret['result'])
  ...     updatePage = site.Pages['Testing Page']
  ...     updatePage.exists
  ...     text = updatePage.edit()
  ...     text = text.replace('[[Category: Testing]]', 
  ...                         '[[Category: My Testing]]')
  ...     ret = updatePage.save(text, summary='Update Category')
  ...     print(ret['result'])
  ... else:
  ...     print """<Site object '...'>
  ... Testing Page
  ... Success
  ... True
  ... Success"""
  ...
  <Site object '...'>
  Testing Page
  Success
  True
  Success

Q: What's the output if login success?

Q: Does the page create / update by mwclient_ trigger 
`MediaWiki hooks`_?
  mwclient_ using MeidaWiki api.php, which will trigger all hooks.

.. _mwclient: https://github.com/mwclient/mwclient
.. _MediaWiki hooks: http://www.mediawiki.org/wiki/Manual:Hooks
.. _MediaWiki api.php: http://www.mediawiki.org/wiki/Manual:Api.php
