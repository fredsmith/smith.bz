#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Smith Family'
SITENAME = u'Smith Family'
SITEURL = ''

PATH = 'content'
THEME = '../pelican-svbtle'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Fred', 'http://fred.smith.bz/'),
        ('Jessica', 'http://jedigurl.com/'),
        ('Andrew', 'http://andrew.smith.bz/'),
        ('Sean', 'http://sean.smith.bz/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
