#!/usr/bin/env python

from urllib.request import urlopen

import certifi
import json
import datetime
import yahoo_fin.stock_info as ys
import yfinance as yf
import utils
import numpy as np
from dateutil import relativedelta

#msft = yf.Ticker("MSFT")
#sector = main.get_stock_type("MSFT")
#print(sector)

symbol = "DIA"

# no date defined, get current price 
date = datetime.datetime.today() - datetime.timedelta(days=1)
    
# get date (+1) in correct format
end_date = date + datetime.timedelta(days=1)

# get date (-5) in correct format
start_date = date - datetime.timedelta(days=10)

result = yf.download(symbol, start_date, end_date, progress=False)
result = result["Adj Close"]
print( result[-1])
