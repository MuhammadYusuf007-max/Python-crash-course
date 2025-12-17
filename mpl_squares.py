import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
squares = [1,4, 9,16,25, 36]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#labels and axes naming
ax.set_title("Square Numbers", fontsize = 25)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square of Value", fontsize = 12)

#size of tick labels
ax.tick_params(labelsize = 12)

plt.show()