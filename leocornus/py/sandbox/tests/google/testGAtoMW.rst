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
  >>> DATE = '2017-05-08'

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
  >>> response = get_report(analytics, VIEW_ID, DATE)

  >>> #print(json.dumps(response, sort_keys=True, indent=2))

  >>> print_response(response)
  ga:pagePath...

Now let dive into the repose data structure.
The rows will have the report data.::

  >>> rows = response['reports'][0]['data']['rows']
  >>> len(rows) > 0
  True

Let's try to go through each rows.::

  >>> pages = []

Here are the structure of each row we will have::

  print(json.dumps(rows[0], indent=2))
  {
    "metrics": [
      {
        "values": [
          "88",
          "337"
        ]
      }
    ],
    "dimensions": [
      "/"
    ]
  }

Now let's get the structure we want.
The built-in funtion int() will convert string to int.::

  >>> for row in rows:
  ...   pages.append([row.get('dimensions', [])[0],
  ...       int(row['metrics'][0]['values'][0]), # this is sessions.
  ...       int(row['metrics'][0]['values'][1])])
  >>> len(pages) > 0
  True

sort the pages by pageviews.::

  >>> sortedPages = sorted(pages, key=lambda page: page[2],
  ...                      reverse=True)
  >>> print(sortedPages[1])

try to save the report as wiki page.::

  >>> from leocornus.py.sandbox.utils_mwclient import MwrcSite
  >>> site = MwrcSite()
  >>> pageTitle = "User:Admin/traffic/opspedia/day-" + DATE + ".json"
  >>> comment = "daily report - " + DATE
  >>> site.create_page(pageTitle, json.dumps(sortedPages), comment)

Testing the utilities function.::

  >>> from leocornus.py.sandbox.utils_google import generate_reports
  >>> dates = ['2017-05-09', '2017-05-10', '2017-05-11']
  >>> generate_reports(analytics, VIEW_ID, dates)
