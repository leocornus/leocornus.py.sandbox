Test class MwrcSite
===================

He are the test plan:

- create a dummy WordPress plugin
- create a .mwrc resource file.
- create a instance of MwrcSite.
- try to get the template values for the dummy plugin.
- verify the values.
- clean up

Set up
------

::

  >>> import os
  >>> from leocornus.py.sandbox.utils_basic import make_test_folder
  >>> from leocornus.py.sandbox.utils_basic import create_file
  >>> testFolder = make_test_folder('test-class');
  >>> print(testFolder)
  /.../test-class

Preparing wp plugin
-------------------

Here is a dummy plugin::

  >>> data = """/**
  ...  * Plugin Name: Plugin something.
  ...  * Plugin URI: http://www.plugin.com
  ...  * Description: plugin two description.
  ...  * Version:  2.0.22
  ...  */
  ...  # *comments**
  ... <?php
  ... phpinfo()"""
  >>> pluginfile = create_file(testFolder, 'plugin.php', data)
  >>> print(pluginfile)
  /.../plugin.php

Preparing mwrc
--------------

Here is a simple mwrc file::

  >>> mwrc_data = """
  ... [mwclient]
  ... path = /wiki/
  ... username = seanchen
  ... password = mypassword
  ...
  ... [template fields]
  ... internet_page: [%(package_uri)s plugin homepage]
  ... download: [http://www.bases.com/repos/%(package_name)s.%(latest_version)s.zip %(package_name)s.%(latest_version)s.zip]
  ...
  ... [template]
  ... wiki_template: {{Feature Infobox
  ...   |name=%(name)s
  ...   |internet_page=%(internet_page)s
  ...   |description=%(description)s
  ...   |latest_version=%(latest_version)s
  ...   |download=%(download)s}}
  ... 
  ... [headers]
  ... latest_version: Version:.*
  ... name: (Plugin|Theme) Name:.*
  ... description: Description:.*
  ... package_uri: (Plugin|Theme) URI:.*
  ... author: Author:.*
  ... author_uri: Author URI:.*
  ...
  ... [headers default]
  ... latest_version: 1.0
  ... """
  >>> mwrc = create_file(testFolder, '.mwrc', mwrc_data)

Test extract and format
-----------------------

test extract headers and get ready the template values::

  >>> from leocornus.py.sandbox.utils_mwclient import MwrcSite
  >>> site = MwrcSite(mwrc)
  >>> values = site.template_values(pluginfile, 'packageone')
  >>> print(values['download'])
  [http://www.bases.com...packageone.2.0.22.zip]

Clean up
--------

Clean up by simply remove the whole test folder::

  >>> import shutil
  >>> shutil.rmtree(testFolder)
  >>> os.path.exists(testFolder)
  False

