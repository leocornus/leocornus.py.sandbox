Test Google Reports API Python Interface
========================================

PENDING...

Follow quicksart for Python: 
https://developers.google.com/admin-sdk/reports/v1/quickstart/python

Save the secret.json as ~/secret.json.

import libs::

  >>> from __future__ import print_function
  >>> import httplib2
  >>> import os

  >>> from apiclient import discovery
  >>> from oauth2client import client
  >>> from oauth2client import tools
  >>> from oauth2client.file import Storage

try:
...     import argparse
...     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
... except ImportError:
...     flags = None

set up some variables::

  >>> flags = None

  >>> SCOPES = 'https://www.googleapis.com/auth/admin.reports.audit.readonly'
  >>> homeFolder = os.path.expanduser('~')
  >>> CLIENT_SECRET_FILE = os.path.join(homeFolder, 'secret.json')
  >>> APPLICATION_NAME = 'Reports API Python Quickstart'

verify ::

  >>> print(CLIENT_SECRET_FILE)
  /home/ubuntu/secret.json
