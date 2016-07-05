#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yu Cheng'
SITENAME = 'yucheng'
SITEURL = 'https://fischcheng.github.io'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Copy from old setting file
GITHUB_URL = 'https://github.com/fischcheng'
EMAIL = "ycheng@rsmas.miami.edu"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = 'en_US'
DEFAULT_PAGINATION = 5
DEFAULT_DATE = (2014, 6, 4, 11, 50, 0)


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('RSMAS', 'http://www.rsmas.miami.edu'),
             ('Julia', "http://julialang.org"),
             ('PyPI','https://pypi.python.org/pypi'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/fischcheng'),
          ('facebook', 'https://www.facebook.com/fischcheng'),
          ('github', GITHUB_URL),)

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook','render_math','pelican_youtube']

# Theme:
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME='flatly'
PYGMENTS_STYLE ='monokai'  #This is for inline highlighting syntaxes

SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True
BOOTSTRAP_FLUID = True
DISQUS_SITENAME = "yucheng"
DISPLAY_BREADCRUMB = True

#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES = True



# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
