from matplotlib import pyplot as plt

x = range(5)
y = [i**3 for i in x]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues,  s = 10)

#Set chart title and label axes.
ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Cube of Value", fontsize = 12)

#Set size of ticl labels
ax.tick_params(labelsize = 12)

plt.show()