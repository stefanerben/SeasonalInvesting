import matplotlib.pyplot as plt
import numpy as np
import datetime

# make data
x = [datetime.date(2018, 1, 9), datetime.date(2018, 1, 10), datetime.date(2018, 1, 11), datetime.date(2018, 1, 12), datetime.date(2020, 1, 13)]
y = [1, 4, 9, 16, 100]

fig, ax = plt.subplots()

ax.plot(x, y, label = "General")
ax.plot(x, y, label = "Seasonal")
plt.legend()
#ax.plot(timeline["general"]["date"], timeline["general"]["value"], linewidth=2.0)

plt.show()
