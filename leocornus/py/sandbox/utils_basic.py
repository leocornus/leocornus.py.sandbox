# utils_basic.py

# the module for basic utilities functions.

# we will follow the Python code style guide,
# function name should be all lowercase letter with underscore.

# doctest only works for docstring, it will not work here.
# the following test will not be tested.
#
# >>> print(2 * 6)
# 12
#

import subprocess

def extract_wp_header(filepath, **default):
    """extract WordPress file header fields values in a dict.

    filepath should be the full path to the file.
    default will provide the available default value.
    We will support the following file header field:

    - Plugin|Theme Name as Name
    - Plugin|Theme URI as URI
    - Description
    - Version
    - Author
    - Author URI
    """
    """
    test the doc test in a py file.

    >>> print(1 + 2)
    3 

    """

    # preparing the patterns.
    patterns = ['Version:.*',
                '(Plugin|Theme) Name:.*',
                'Description:.*',
                '(Plugin|Theme) URI:.*',
                'Author:.*',
                'Author URI:.*'
               ]

    # return as a dict.
    ret = {}
    for pattern in patterns:
        # get the field name:
        field_name = pattern.split(b":")[0]
        # the grep pattern.
        grep_pattern = """grep -oE '%s' %s""" % (pattern, filepath)

        try:
            value = subprocess.check_output(grep_pattern, shell=True)
            # only split the first ":"
            value = value.strip().split(b":", 1)
            ret[field_name] = value[1].strip()
        except subprocess.CalledProcessError:
            # could NOT find the pattern.
            if default.has_key(field_name):
                ret[field_name] = default[field_name]
            else:
                ret[field_name] = ""

    return ret