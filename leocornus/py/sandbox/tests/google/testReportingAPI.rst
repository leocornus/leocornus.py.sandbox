Test Google Reporting API Python Interface
==========================================

Follow quicksart for Python: 
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/installed-py

Save the secret.json as ~/secret.json.

import libs::

  >>> import os
  >>> import argparse
  >>> from apiclient.discovery import build
  >>> import httplib2
  >>> from oauth2client import client
  >>> from oauth2client import file
  >>> from oauth2client import tools

set up some variables::
  >>> SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
  >>> DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
  >>> homeFolder = os.path.expanduser('~')
  >>> CLIENT_SECRETS_PATH = os.path.join(homeFolder, 'secret.json')
  >>> VIEW_ID = '41055556' 

verify ::

  >>> print(CLIENT_SECRETS_PATH)
  /home/ubuntu/secret.json
