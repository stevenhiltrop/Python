# -*- coding: utf-8 -*-
from urllib.request import urlopen

import yfinance as yf
from bs4 import BeautifulSoup

tickers = str()

# TODO 1. Get all earningreport tickers

source = 'https://earningswhispers.com/calendar'
with urlopen(source) as response:
    page = response.read()

soup = BeautifulSoup(page, 'html.parser')
whisper_tickers = soup.find_all('div', attrs={'class': 'ticker'})

for ticker in whisper_tickers:
    tickers += "{} ".format(ticker.text)

# TODO 2. Get financial data through API calls

tickers = yf.Tickers(tickers)

# TODO 3. Make conclusions
