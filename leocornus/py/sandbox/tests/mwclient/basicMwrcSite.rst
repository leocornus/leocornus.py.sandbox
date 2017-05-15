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
