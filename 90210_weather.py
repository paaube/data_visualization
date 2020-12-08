import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/90210.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(date)
        highs.append(high)
        lows.append(low)

# plot the temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format the plot
ax.set_title("Min and Max temperatures at 90210", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

