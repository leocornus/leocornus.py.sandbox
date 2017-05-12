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

  >>> from leocornus.py.sandbox.utils_google import initialize_analyticsreporting

function to get report::

  >>> def get_report(analytics):
  ...   # Use the Analytics Service Object to query the Analytics Reporting API V4.
  ...   return analytics.reports().batchGet(
  ...       body={
  ...         'reportRequests': [
  ...         {
  ...           'viewId': VIEW_ID,
  ...           'pageSize': 10000,
  ...           'dateRanges': [{'startDate': '2017-05-01', 'endDate': '2017-05-01'}],
  ...           'metrics': [
  ...             {'expression': 'ga:sessions'},
  ...             {'expression': 'ga:pageviews'}
  ...           ],
  ...           'dimensions': [
  ...             {
  ...               'name': 'ga:pagePath'
  ...             }
  ...           ],
  ...         }]
  ...       }
  ...   ).execute()

utility function to print the response::

  >>> def print_response(response):
  ...   """Parses and prints the Analytics Reporting API V4 response"""
  ... 
  ...   for report in response.get('reports', []):
  ...     columnHeader = report.get('columnHeader', {})
  ...     dimensionHeaders = columnHeader.get('dimensions', [])
  ...     metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
  ...     rows = report.get('data', {}).get('rows', [])
  ... 
  ...     for row in rows:
  ...       dimensions = row.get('dimensions', [])
  ...       dateRangeValues = row.get('metrics', [])
  ... 
  ...       for header, dimension in zip(dimensionHeaders, dimensions):
  ...         print header + ': ' + dimension
  ... 
  ...       for i, values in enumerate(dateRangeValues):
  ...         print 'Date range (' + str(i) + ')'
  ...         for metricHeader, value in zip(metricHeaders, values.get('values')):
  ...           print metricHeader.get('name') + ': ' + value

Now let's execute it...::

  >>> analytics = initialize_analyticsreporting(KEY_FILE_LOCATION, SCOPES)
  >>> response = get_report(analytics)
  >>> len(response['reports'][0]['data']['rows'])

  >>> #print(json.dumps(response, sort_keys=True, indent=2))

  >>> print_response(response)
  ga:pagePath...
