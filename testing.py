#!/usr/bin/env python

from urllib.request import urlopen

import certifi
import json
import datetime
import yahoo_fin.stock_info as ys
import yfinance as yf
import main
#msft = yf.Ticker("MSFT")
#sector = main.get_stock_type("MSFT")
#print(sector)


price = main.get_price_for_symbol("MSFT", date=datetime.date(2022, 1, 9) )
print(price)