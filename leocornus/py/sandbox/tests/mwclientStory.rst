Story about mwclient
====================

This is a basic learning story about mwclient_.

.. contents::
   :depth: 5

Query Wikipedia
---------------

This is the basic usage of mwclient_. 
The following testing is mainly based on mwclient_ tutorial.

Try to connect to wikipedia site::

  >>> import mwclient
  >>> site = mwclient.Site('en.wikipedia.org')
  >>> site
  <Site object 'en.wikipedia.org/w/'>

Try to get the Special:Version page as a quick test::

  >>> version = site.Pages['Special:Version']
  >>> version.text()
  u''

.. _mwclient: https://github.com/mwclient/mwclient
