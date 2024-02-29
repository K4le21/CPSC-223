import matplotlib.pyplot as plt

x_axis = []
y_axis = []

for i in range(5000):
    x_axis.append(i)

for i in range(5000):
    y_axis.append(i**3)

plt.plot(x_axis, y_axis)
plt.show()