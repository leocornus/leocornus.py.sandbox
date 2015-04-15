Story for ConfigParser
======================

.. note::

   the ConfigParser_ module has been renmae to configparser_ in 
   Python 3. the 2to3_ tool will automatically adapt imports
   when converting your sources to Python 3.

As of the module name change, we will using the following way 
to import configparser module::

  >>> try:
  ...     import ConfigParser as configparser
  ... except ImportError:
  ...     import configparser

Create a ConfigParser object::

  >>> config = configparser.ConfigParser()
  >>> config.sections()
  []

Basic
-----

Here ae some basic things:

- configuration file support multiple-line values,
  check `RFC 822 Section 3.1.1`_ for details.
- using **'#'** or **';'** for comments.

Prepare testing
---------------

Generally import and create testing folder::

  >>> import os
  >>> from leocornus.py.sandbox.utils_basic import make_test_folder
  >>> from leocornus.py.sandbox.utils_basic import create_file
  >>> testFolder = make_test_folder('test-config');
  >>> print(testFolder)
  /.../test-config

Question: Can config file handle multi-line values?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The config file handle multiple line value very will.
Check the following testing for details.
Get ready some data for testing::

  >>> config_data = """
  ... [simple]
  ... keyone: value one
  ... key_pattern: (Plugin|Theme) Name:.*
  ... keytwo: multipile line testing
  ...         this is the second line.
  ...  this is the third line
  ... keythree:
  ...  multipile line is different 
  ...  with some format string ||(abc)s,
  ...  one more line ||(cde)s
  ...  format.
  ... """
  >>> filename = create_file(testFolder, 'test.cfg', config_data)

read the config file and verify the values::

  >>> filename = config.read(filename)
  >>> print(config.get('simple', 'keyone'))
  value one
  >>> print(config.get('simple', 'key_pattern'))
  (Plugin|Theme) Name:.*
  >>> print(config.get('simple', 'keytwo'))
  multipile line testing
  this is the second line.
  this is the third line
  >>> template = config.get('simple', 'keythree')
  >>> print template
  <BLANKLINE>
  multipile line is different
  with some format string ||(abc)s,
  one more line ||(cde)s
  format.

replace **'||'** with **'%'**, so we could formt the string::

  >>> template = template.replace('||', "%")
  >>> print(template)
  <BLANKLINE>
  multipile line is different
  with some format string %(abc)s,
  one more line %(cde)s
  format.
  >>> print(template % dict(abc="aaa", cde="bbb"))
  <BLANKLINE>
  multipile line is different
  with some format string aaa,
  one more line bbb 
  format.

Case Study: WordPress header to MediaWiki template
--------------------------------------------------

The requirment is to fill out a MediaWiki template with
values from WordPress header fields.
The proposal is:

- save the header field to template field mapping in a config file.
- save the wiki template in a separate file.

Here are some testing data::

  >>> mwrc_data = """
  ... [mwclient]
  ... host = wiki.site.domain.com
  ... path = /wiki/
  ... username = seanchen
  ... password = mypassword
  ...
  ... [template]
  ... base_url: http://my.repo.com/repos
  ... homepage_label: plugin homepage 
  ... wiki_template: {{Feature Infobox
  ...   |name=||(name)s
  ...   |internet_page=||(internet_page)s
  ...   |description=||(description)s
  ...   |latest_version=||(latest_version)s
  ...   |download=||(download)s}}
  ... 
  ... [headers]
  ... latest_version: Version:.*
  ... name: (Plugin|Theme) Name:.*
  ... description: Description:.*
  ... package_uri: (Plugin|Theme) URI:.*
  ... author: Author:.*
  ... author_uri: Author URI:.*
  ... """
  >>> mwrc = create_file(testFolder, '.mwrc', mwrc_data)

Explore the config file::

  >>> filename = config.read(mwrc)
  >>> print(filename[0] == mwrc)
  True

items function will return the whole section in pairs like
**(key, value)**::

  >>> headers = config.items('headers')
  >>> print(headers[0])
  ('latest_version', 'Version:.*')

Clean up
--------

Clean up by simply remove the whole test folder::

  >>> import shutil
  >>> shutil.rmtree(testFolder)
  >>> os.path.exists(testFolder)
  False

.. _ConfigParser: https://docs.python.org/2/library/configparser.html
.. _configparser: https://docs.python.org/3/library/configparser.html
.. _2to3: https://docs.python.org/2/glossary.html#term-to3
.. _RFC 822 Section 3.1.1: http://tools.ietf.org/html/rfc822.html#section-3.1
