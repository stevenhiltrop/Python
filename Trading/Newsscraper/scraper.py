# -*- coding: utf-8 -*-
from urllib.request import urlopen

import yfinance
from bs4 import BeautifulSoup
from termcolor import colored

tickers = str()
stocks = list()


def create_dataframe(stock):
    result = dict()
    value = stock.get("previousClose")
    volume = stock.get("volume")
    float = stock.get("floatShares")
    marketcap = stock.get("marketCap")

    if 1000000 < volume < 1000000:
        result["volume"] = colored(volume, "green")
    else:
        result["volume"] = colored(volume, "red")


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
    ticker = yfinance.Tickers(tickers)
    # https://github.com/ranaroussi/yfinance

    # print(colored("[-] Downloading ticker data", "yellow"))
    # data = yf.download(tickers, period="1d", group_by="ticker")
    # print(colored("[+] Done!", "green"))

    print(colored("[-] Getting information on each ticker (this might take a while)", "yellow"))
    for ticker in tickers.tickers:
        stocks.append(ticker.info)

# TODO 3. Set filter criteria
    # check_criteria()


# TODO 4. Make conclusions
    # create_dataframe(ticker)

else:
    print(colored("[X] Could not scrape website", "red"))
