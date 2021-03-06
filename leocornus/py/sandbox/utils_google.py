# utils_google.py

# the module for google utilities functions.

# we will follow the Python code style guide,
# function name should be all lowercase letter with underscore.

# doctest only works for docstring, it will not work here.
# the following test will not be tested.
#
# >>> print(2 * 6)
# 12
#

# dependences:

import json
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from leocornus.py.sandbox.utils_mwclient import MwrcSite

def init_gareporting(key_file, scopes):
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      key_file, scopes)

  # Build the service object.
  analytics = build('analytics', 'v4', credentials=credentials)

  return analytics

# sample function to execute the batch get report.
# the main purpose here is for demostration.
# normally we will use the batchGet directly.
# the challenge part it get ready the reportRequests object.
def get_report(analytics, view_id, date):
  # Use the Analytics Service Object to query the Analytics Reporting API V4.
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': view_id,
          'pageSize': 10000,
          'dateRanges': [{'startDate': date, 'endDate': date}],
          'metrics': [
            {'expression': 'ga:sessions'},
            {'expression': 'ga:pageviews'}
          ],
          'dimensions': [
            {
              'name': 'ga:pagePath'
            }
          ],
        }]
      }
  ).execute()

# utility function to print the response, 
# it show the data structure of the response object.
def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response"""

  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    rows = report.get('data', {}).get('rows', [])

    for row in rows:
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print header + ': ' + dimension

      for i, values in enumerate(dateRangeValues):
        print 'Date range (' + str(i) + ')'
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print metricHeader.get('name') + ': ' + value

# generate the report for a date range.
def generate_reports(analytics, view_id, date_range):
    """here are what we will do:
    * query report,
    * parse into prefered format.
    * sort into wiki page.
    the date_range will be a list of date, for example:
    ['2017-05-05', [2017-05-06']
    """

    for date in date_range:
        response = get_report(analytics, view_id, date)
        rows = response['reports'][0]['data']['rows']
        pages = []
        for row in rows:
            pages.append([row['dimensions'][0],
                  int(row['metrics'][0]['values'][0]), 
                  int(row['metrics'][0]['values'][1])])
        # sort by pageviews.
        sortedPages = sorted(pages, key=lambda page: page[2],
                             reverse=True)
        # sort the result.
        site = MwrcSite()
        pageTitle = "User:Admin/traffic/opspedia/day-" + date + ".json"
        comment = "daily report - " + date 
        site.create_page(pageTitle, json.dumps(sortedPages), comment)
