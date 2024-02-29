import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
station = []
name = []
date = []
prcp = []
tavg = []
tmax = []
tmin = []


with open(filename) as f:
    heading = next(f)
    data = csv.reader(f, delimiter=',')

    for row in data:
        station.append(row[0])
        name.append(row[1])
        date.append(row[2])
        prcp.append(row[3])
        tavg.append(row[4])
        tmax.append(row[5])
        tmin.append(row[6])

    x_axis = []
    y_axis = []

    for i in range(len(date)):
        x_axis.append(i)

    y_axis = prcp.copy()

    fig, ax = plt.subplots()

    ax.set_xlabel("Days since 2018-01-01")
    ax.set_ylabel("Rainfall")

    ax.tick_params(axis='both', which='major')


    plt.scatter(x_axis, y_axis)

    plt.show()
