# 9. Write a Python program to display the current axis limits values and set new axis values.

import matplotlib.pyplot  as plt

x, y = range(50), [value*3 for value in range(50)]

plt.plot(x, y)
plt.title("Draw a line")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

print(plt.axis())
plt.axis([0,100, 0, 200])
plt.show()