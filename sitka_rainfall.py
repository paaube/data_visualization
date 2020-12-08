import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    
    dates, rainfall = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(date)
        rainfall.append(rain)

# plot the rainfall
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue')

# format plot
ax.set_title("Rainfall in Sitka", fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

