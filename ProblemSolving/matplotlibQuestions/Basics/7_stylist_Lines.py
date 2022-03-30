# 7. Write a Python program to plot two or more lines with different styles.

import matplotlib.pyplot as plt

x1, y1, x2, y2 = [10,20,30], [20,40,10], [10,20,30], [40,10,30]

plt.title("Plot with two or more lines with different stypes")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.plot(x1, y1, linestyle="dotted", linewidth=3, color="blue", label="line1-dotted")
plt.plot(x2,y2, linestyle="dashed", linewidth=5, color="red", label="line2-dashed")
plt.legend()
plt.show()
