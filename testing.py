#!/usr/bin/env python

import yfinance as yf
import main

from urllib.request import urlopen

import certifi
import json

#msft = yf.Ticker("MSFT")
#sector = main.get_stock_type("MSFT")
#print(sector)


symbols, weights = main.get_sp500_index()

for symbol in symbols:
    if "," in symbol:
        print(symbol)