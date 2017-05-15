Basic test cases for MwrcSite
=============================

Import the utility functions from utils.::

  >>> from leocornus.py.sandbox.utils_mwclient import mw_create_page

Get ready the wiki page.::

  >>> pageTitle = 'user:Seanchen/data/somedata.json'
  >>> pageContent = """[
  ...  ["/site/page", 234, 1234],
  ...  ["/two/one", 123, 2345]
  ... ]"""

save to wiki::

  >>> mw_create_page(pageTitle, pageContent)

Try the class::

  >>> from leocornus.py.sandbox.utils_mwclient import MwrcSite
  >>> site = MwrcSite()

set different page title.::

  >>> pageTitle = 'User:Seanchen/data/newtitle.json'
  >>> site.create_page(pageTitle, pageContent, 'create page')

Check the case with content change.::

  >>> pageContent = """[
  ...  ["/site/page", 234, 1234],
  ...  ["/two/one", 123, 2345],
  ...  ["/two/three", 23, 4345]
  ... ]"""
  >>> site.create_page(pageTitle, pageContent, 'add one more')
