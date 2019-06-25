import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)
# plt.show()

# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
# plt.scatter(x_value, y_value, s=100)
#
x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)
# plt.scatter(x_value, y_value,edgecolors='none', s=40)

# #
plt.plot(x_value, y_value, linewidth=5)
#
# 设置标题
plt.title("square Numbers", fontsize=24)
plt.xlabel('value', fontsize=24)
plt.ylabel('square of value', fontsize=24)
#
# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
