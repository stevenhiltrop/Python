# -*- coding: utf-8 -*-
from urllib.request import urlopen

import pandas
import yfinance
from bs4 import BeautifulSoup
from termcolor import colored

source = 'https://earningswhispers.com/calendar'
tickers = str()
stocks = list()


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


def get_stock_information(stock):
    result = dict()
    try:
        result["name"] = stock.ticker
        result["price"] = stock.info.get("previousClose")
        result["float"] = stock.info.get("floatShares")
        result["volume"] = stock.info.get("volume")
        result["marketcap"] = stock.info.get("marketCap")
        print(colored(f"{stock.ticker} done.", "green"))
    except:
        print(colored(f"{stock.ticker} failed.", "red"))

    # if 5 < result["price"] < 100:
    #     result["price"] = colored(f"{} done.", "green")

    return result

print(colored("[-] Connecting to earningswhispers.com...", "yellow"))

with urlopen(source) as response:
    page = response.read()

if page:
    print(colored("[+] Success!", "green"))
    soup = BeautifulSoup(page, 'html.parser')
    print(colored("[-] Scrapping tickers ...", "yellow"))
    whisper_tickers = soup.find_all('div', attrs={'class': 'ticker'})

    for ticker in whisper_tickers:
        tickers += f"{ticker.text} "
    print(colored(f"[+] Tickers: {tickers.replace(' ', ', ')}", "green"))

    tickers = yfinance.Tickers(tickers)

    print(colored("[-] Getting information on each ticker (this might take a while)", "yellow"))
    for ticker in tickers.tickers:
        ticker = get_stock_information(ticker)
        stocks.append(ticker)

    # TODO 3. Set filter criteria


    # TODO 4. Make conclusions
    print(pandas.DataFrame(stocks).to_string(index=False))

else:
    print(colored("[X] Could not scrape website", "red"))
