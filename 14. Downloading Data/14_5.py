import csv
from datetime import datetime 

import matplotlib.pyplot as plt

def get_temp_indices(header):
    index = []
    i = 0
    for x in header:
        if x == "TMAX" or x == "TMIN": 
            index.append(i)
        i += 1
    return tuple(index)

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    tempindex = get_temp_indices(header_row)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:													# new code
            high = int(row[tempindex[0]])
            low = int(row[tempindex[1]])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

maxrange = max(highs) + 10
minrange = min(lows) - 10



# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()


ax.scatter(dates, highs, c='red', alpha = 0.5) # new code
ax.scatter(dates, lows, c='blue', alpha = 0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA\nAt station USC00042319" # new code
ax.set_title(title, fontsize=14)

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() 
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(minrange, maxrange)


plt.show()