# -*- coding: utf-8 -*-
import ssl
import urllib.request

import certifi
from bs4 import BeautifulSoup

tickers = list()
# TODO 1. Get all earningreports
source = 'https://earningswhispers.com/calendar'
with urllib.request.urlopen(source, context=ssl.create_default_context(cafile=certifi.where())) as response:
    page = response.read()

soup = BeautifulSoup(page, 'html.parser')
whisper_tickers = soup.find_all('div', attrs={'class': 'ticker'})

for ticker in whisper_tickers:
    tickers.append(ticker.text)

####################################################################################

source = 'https://www.marketwatch.com/tools/earningscalendar'
with urllib.request.urlopen(source, context=ssl.create_default_context(cafile=certifi.where())) as response:
    page = response.read()

soup = BeautifulSoup(page, 'html.parser')
marketwatch_tickers = soup.find_all('td')

for ticker in marketwatch_tickers:
    if ticker.text.isupper():
        tickers.append(ticker.text)

# TODO 2. Check if they have enough volume
