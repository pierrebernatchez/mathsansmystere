
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pierre Bernatchez'
SITENAME = u'Math Sans Mystère'
#SITEURL = u'http://www.bernatchez.net/static_testsite'
SITEURL = u'http://127.0.0.1:8000'

THEME = u"/home/ubuntu/pelican-themes/lightweight"
#THEME = u"/home/ubuntu/pelican-themes/sneakyidea"
#THEME = u"/home/ubuntu/pelican-themes/basic"
#THEME = u"/home/ubuntu/pelican-themes/cebong"

TIMEZONE = 'America/Toronto'

PAGE_ORDER_BY = 'slug'
ARTICLE_ORDER_BY = 'slug'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS=['images', 'compilations', 'tarballs', 'sitepdfs' ]
