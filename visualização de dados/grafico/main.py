import matplotlib.pyplot as plt

x_values = range(1, 5)
y_values = [x**3 for x in x_values]

x_values_green = range(1, 5000)
y_values_green = [x**3 for x in x_values_green]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=1000)
ax.scatter(x_values_green, y_values_green, c=y_values_green, cmap=plt.cm.Purples, s=10)

ax.set_title("Squares numbers", fontsize=24)
ax.set_xlabel("value", fontsize=24)
ax.set_ylabel("square of value", fontsize=24)
ax.tick_params(labelsize=14)
# ax.axis([0, 100, 0, 200])
# ax.ticklabel_format(style='plain')
plt.show()
# print(plt.style.available)