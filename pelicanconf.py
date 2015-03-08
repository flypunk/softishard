#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pavel Suchman'
SITENAME = u'Soft is hard'
TAGLINE = 'A blog about system architecture, software, cloud and devops'
SITEURL = ''

THEME = 'pure'
PATH = 'content'
COVER_IMG_URL = 'http://images.noopsware.com.s3.amazonaws.com/10880155_ml.jpg'
TIMEZONE = 'Asia/Jerusalem'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'
DISQUS_SITENAME = "softishard"
GOOGLE_ANALYTICS = 'UA-39619824-6'
TWITTER_USERNAME = 'pavelsuchman'

#https://softishard.disqus.com/admin/settings/universalcode/


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
         ('You can modify those links in your config file', '#'),)

SOCIAL = (('twitter', 'http://twitter.com/pavelsuchman'),
          ('github', 'http://github.com/flypunk'),
          ('LinkedIN', 'http://linkedin.com/in/pavelsuchman'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
