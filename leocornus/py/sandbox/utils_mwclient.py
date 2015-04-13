# utils_mwclient.py

"""Utility functions to access mwlient_

This will be module __doc__
"""
"""
This is additional docs

Try some testing here:

>>> print(2 * 5)
10

we should be able to the module doc like following:

>>> from leocornus.py.sandbox import utils_mwclient
>>> print(utils_mwclient.__doc__)
Utility functions to access mwlient_
<BLANKLINE>
This will be module __doc__

"""

import os

# Python version 3.0 using all lowercase module name.
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"


# the following functions are rewrite from mwclientBasic.rst

def mw_get_login(mwrc=None):
    """Get MediaWiki site's login info from the given mwrc file.
    The default is ~/.mwrc, if none is specified.

    This function will return a dict objet with the following keys:

    :host: domain name for the MediaWiki site.
    :path: the uri to MediaWiki site.
    :username: MediaWiki site user login.
    :password: MediaWiki site user password.
    """
    """
    Here is a quick test:

    >>> from leocornus.py.sandbox.utils_mwclient import mw_get_login 
    >>> print(mw_get_login)
    <function mw_get_login at ...>

    """

    if(merc == None):
        # try to get the mw login info from default location:
        # ~/.mwrc 
        home_folder = os.path.expanduser('~')
        mwrc = os.path.join(home_folder, '.mwrc')
    # set the empty dict.
    mwinfo = {}

    if os.path.exists(mwrc):
        rc = configparser.ConfigParser()
        # the config parser read method will return the filename
        # in a list.
        filename = rc.read(mwrc)
        mwinfo['host'] = rc.get('mwclient', 'host')
        mwinfo['path'] = rc.get('mwclient', 'path')
        mwinfo['username'] = rc.get('mwclient', 'username')
        mwinfo['password'] = rc.get('mwclient', 'password')
        # TODO: need check if those values are set properly!

    return mwinfo

# create a wiki page.
def mw_create_page(title, content, categories):
    """Create a MediaWiki page.
    """
