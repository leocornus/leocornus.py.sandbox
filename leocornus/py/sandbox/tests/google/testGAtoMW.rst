try to query GA report and store it as MediaWiki page
=====================================================

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

function to get report::

  >>> from leocornus.py.sandbox.utils_google import get_report

utility function to print the response::

  >>> from leocornus.py.sandbox.utils_google import print_response 

Now let's execute it...::

  >>> analytics = init_gareporting(KEY_FILE_LOCATION, SCOPES)
  >>> response = get_report(analytics, VIEW_ID)
  >>> len(response['reports'][0]['data']['rows'])

  >>> #print(json.dumps(response, sort_keys=True, indent=2))

  >>> print_response(response)
  ga:pagePath...
