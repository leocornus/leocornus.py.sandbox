Basic cases for requests
========================

import requests::

  >>> import requests
  >>> requests
  <module 'requests' from '...>

Let's try to get the homepage of github.com::

  >>> github = requests.get('http://www.github.com')
  >>> github.status_code
  200
  >>> github.encoding
  'utf-8'
  >>> github
  <Response [200]>
  >>> github.text
  u'\n\n\n<!DOC...'

the response of requests get also have JSON format::
