import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [i**2 for i in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,  s = 10)

#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square of Value", fontsize = 12)

#Set size of ticl labels
ax.tick_params(labelsize = 12)

#Set range of each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png', bbox_inches='tight')