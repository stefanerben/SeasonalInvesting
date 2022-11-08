import matplotlib.pyplot as plt
import numpy as np
import datetime

plt.style.use('_mpl-gallery')

# make data
x = [datetime.date(2018, 1, 9), datetime.date(2018, 1, 10), datetime.date(2018, 1, 11), datetime.date(2018, 1, 12), datetime.date(2020, 1, 13)]
y = [1, 4, 9, 16, 100]

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()