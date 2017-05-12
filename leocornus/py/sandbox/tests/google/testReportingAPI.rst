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

define some functions::

  >>> def initialize_analyticsreporting():
  ...   """Initializes the analyticsreporting service object.
  ... 
  ...   Returns:
  ...     analytics an authorized analyticsreporting service object.
  ...   """
  ...   # Parse command-line arguments.
  ...   parser = argparse.ArgumentParser(
  ...       formatter_class=argparse.RawDescriptionHelpFormatter,
  ...       parents=[tools.argparser])
  ...   flags = parser.parse_args([])
  ... 
  ...   # Set up a Flow object to be used if we need to authenticate.
  ...   flow = client.flow_from_clientsecrets(
  ...       CLIENT_SECRETS_PATH, scope=SCOPES,
  ...       message=tools.message_if_missing(CLIENT_SECRETS_PATH))
  ... 
  ...   # Prepare credentials, and authorize HTTP object with them.
  ...   # If the credentials don't exist or are invalid run through the native client
  ...   # flow. The Storage object will ensure that if successful the good
  ...   # credentials will get written back to a file.
  ...   storage = file.Storage('analyticsreporting.dat')
  ...   credentials = storage.get()
  ...   if credentials is None or credentials.invalid:
  ...     credentials = tools.run_flow(flow, storage, flags)
  ...   http = credentials.authorize(http=httplib2.Http())
  ... 
  ...   # Build the service object.
  ...   analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)
  ... 
  ...   return analytics

function to get report::

  >>> def get_report(analytics):
  ...   # Use the Analytics Service Object to query the Analytics Reporting API V4.
  ...   return analytics.reports().batchGet(
  ...       body={
  ...         'reportRequests': [
  ...         {
  ...           'viewId': VIEW_ID,
  ...           'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
  ...           'metrics': [{'expression': 'ga:sessions'}]
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

  >>> analytics = initialize_analyticsreporting()
  >>> response = get_report(analytics)
  >>> print_response(response)
