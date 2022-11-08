#!/usr/bin/env python

from urllib.request import urlopen

import certifi
import json
import datetime
import yahoo_fin.stock_info as ys
import yfinance as yf
import utils
from dateutil import relativedelta

#msft = yf.Ticker("MSFT")
#sector = main.get_stock_type("MSFT")
#print(sector)



print(int(datetime.datetime.utcnow().timestamp()))

starting_date =  datetime.date(2022, 1, 9)
print(utils.datetime_to_int(starting_date))
ending_date = datetime.date.today()
current_date = starting_date

utils.start_progress("Get Stock Types...")

while current_date < ending_date:
            
    utils.progress(2 / 9 * 100)
    #current_date = current_date + datetime.timedelta(days=1)
    current_date = current_date + relativedelta.relativedelta(months=1, day=1)
    print(current_date)

utils.end_progress()



