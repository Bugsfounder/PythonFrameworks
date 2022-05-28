# 5. Write a Python program to plot two or more lines on same plot with suitable legends of each line.

import matplotlib.pyplot as plt

x1, y1, x2, y2 = [10,20,30],[20,40,10], [10,20,30], [40,10,30]

plt.plot(x1,y1, label="line 1" )
plt.plot(x2, y2, label="line 2")
plt.legend()
plt.title("Two or more lines on same plot with suitable legends")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.show()


