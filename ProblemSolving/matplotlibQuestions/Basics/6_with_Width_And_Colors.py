# 6. Write a Python program to plot two or more lines with legends, different widths and colors.

import matplotlib.pyplot as plt

x1, y1, x2, y2 = [10,20,30], [20,40, 10], [10,20,30], [40,10,20]

plt.title("Two or more lines with different widths and colors with suitable legends")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.plot(x1,y1, label="line1-width-3", linewidth=3, color='red')
plt.plot(x2,y2, label="line2-width-5", linewidth=5, color="blue")
plt.legend()
plt.show()