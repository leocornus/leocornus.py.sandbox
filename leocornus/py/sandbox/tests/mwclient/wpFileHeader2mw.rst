Extract WordPress File Header and Save as Wiki Page
===================================================

This story is about extract names and values from `WordPress file
header`_ and save them as a MediaWiki page.

Important Assumptions
---------------------

- The value for WordPress header field  will be all in one line.

Header to Wiki Template Mapping
-------------------------------

We will use wiki template to save those file header fields.
Here is a list of WordPress file headers we will extract the values:

- Plugin/Theme Name
- Plugin/Theme URI
- Description
- Version

Here is an example of Wiki template::

  {{Feature Infobox
  |name = BP Group Documents
  |implementation = Document Management for BuddyPress Group, 
  |type = WordPress Network Plugin
  |description = BP Group Documents creates a page ...
  |latest_version = 1.8
  |internet_page = [http://wordpress.org/ Plugin Homepage]
  |download = [https://downloads.wordpress.org/bpdoc.zip pbdoc.zip]

Here are the mapping.

================== ============================================
Wordpress Header   Wiki Template Field
================== ============================================
Plugin/Theme Name  name
                   This will be also the page title.
Plugin/Theme URI   internet_page
                   This should be Wiki syntax with proper label
Description        description
Version            latest_version
================== ============================================

.. _WordPress file header: https://codex.wordpress.org/File_Header
