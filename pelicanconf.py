#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Edmund Kent-Hazledine'
SITENAME = 'Ed Kent-Hazledine'
SITEURL = 'https://edthecoder.dev'
THEME = './theme'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Full Stack Python', 'https://www.fullstackpython.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
