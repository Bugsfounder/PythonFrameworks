# 8. Write a Python program to plot two or more lines and set the line markers.

import matplotlib.pyplot as plt

x1, y1 = [1, 4, 5, 6, 7], [2, 6, 3, 6, 3]

plt.title("Display Marker")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.plot(x1,y1, marker="o", linestyle="dashdot", color='red', linewidth=3, markersize=12,  markerfacecolor="blue")
plt.show()