# -*- coding: utf-8 -*-
import urllib.request
import ssl
import certifi

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
with urllib.request.urlopen(quote_page, context=ssl.create_default_context(cafile=certifi.where())) as response:
    html = response.read()
