# -*- coding: utf-8 -*-
from urllib.request import urlopen

import yfinance as yf
from bs4 import BeautifulSoup
from termcolor import colored

tickers = str()

# TODO 1. Get all earningreport tickers

source = 'https://earningswhispers.com/calendar'

print(colored("[-] Connecting to earningswhispers.com...", "yellow"))

with urlopen(source) as response:
    page = response.read()
if page:
    print(colored("[+] Success!", "green"))
    soup = BeautifulSoup(page, 'html.parser')
    print(colored("[-] Scrapping tickers ...", "yellow"))
    whisper_tickers = soup.find_all('div', attrs={'class': 'ticker'})

    for ticker in whisper_tickers:
        tickers += "{} ".format(ticker.text)
    print(colored("[+] Tickers: {}", "green").format(tickers.replace(" ", ", ")))
    # TODO 2. Get financial data through API calls
    # https://github.com/ranaroussi/yfinance

    print(colored("[-] Getting information on each ticker (this might take a while)", "yellow"))
    data = yf.download(tickers, start="2017-01-01", end="2017-04-30", group_by="ticker")

    # print(colored("[-] Getting information on each ticker (this might take a while)", "yellow"))
    # for ticker in tickers.tickers:
    #     ticker = ticker.info
    #
    #     value = ticker.get("previousClose")
    #     volume = ticker.get("volume")
    #     float = ticker.get("floatShares")
    #     marketcap = ticker.get("marketCap")

# TODO 3. Set filter criteria

# TODO 4. Make conclusions

else:
    print(colored("[X] Could not scrape website", "red"))
