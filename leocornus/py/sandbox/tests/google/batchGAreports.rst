quick test for batch report and save
====================================

Follow quicksart for Python: 
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

Save the client-secret.json as ~/client-secret.json.

import libs::

  >>> import os
  >>> import json

set up some variables::

  >>> SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
  >>> homeFolder = os.path.expanduser('~')
  >>> KEY_FILE_LOCATION = os.path.join(homeFolder, 'client-secret.json')
  >>> VIEW_ID = '41055556' 

verify ::

  >>> print(KEY_FILE_LOCATION)
  /home...secret.json

define some functions, initialize and connect to Google.::

  >>> from leocornus.py.sandbox.utils_google import init_gareporting
  >>> analytics = init_gareporting(KEY_FILE_LOCATION, SCOPES)

Testing the utilities function.::

  >>> from leocornus.py.sandbox.utils_google import generate_reports
  >>> dates = [
  ...    '2017-05-15', 
  ... ]
  >>> generate_reports(analytics, VIEW_ID, dates)
