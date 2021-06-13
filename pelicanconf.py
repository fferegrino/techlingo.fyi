#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'antonio.feregrino@gmail.com'
SITENAME = 'TechLingo.fyi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'

ARTICLE_ORDER_BY = 'reversed-title'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True