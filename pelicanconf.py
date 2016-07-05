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
DEFAULT_PAGINATION = 10
DEFAULT_DATE = (2014, 6, 4, 11, 50, 0)


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Sidebar
LINKS = (('RSMAS', 'http://www.rsmas.miami.edu'),
             ('邁阿密網球筆記', "http://www.sportsv.net/authors/fischcheng"))#,
SOCIAL = (('twitter', 'http://twitter.com/fischcheng'),
          ('facebook', 'https://www.facebook.com/fischcheng'),
          ('github', GITHUB_URL),)

DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_TAGS_INLINE=True
#TAG_CLOUD_MAX_ITEMS = 10


# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook','render_math','pelican_youtube','tag_cloud']

# Theme related:
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME='flatly'
PYGMENTS_STYLE ='monokai'  #This is for inline highlighting syntaxes


ABOUT_ME = "I'm a PhD student focusing on Agulhas leakage and its climatic impact. \
<p>RSMAS / University of Miami <br>\
<a href=\"mailto:yucheng@rsmas.miami.edu\">yucheng@rsmas.miami.edu</a> </p>"
AVATAR = "/images/headshot.jpg"



SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True
BOOTSTRAP_FLUID = True

DISQUS_SITENAME = "yucheng"
#DISQUS_DISPLAY_COUNTS = True
DISPLAY_BREADCRUMB = True



# static paths will be copied under the same name
STATIC_PATHS = ["images","extra/custom.css"]
BANNER = 'images/WP_20130331_11_33_12_Panorama.jpg'
BANNER_SUBTITLE = 'Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better.'
#BANNER_ALL_PAGES = True
EXTRA_PATH_METADATA = {'extra/custom.css': {'path': 'static/custom.css'}}
CUSTOM_CSS = 'static/custom.css'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
