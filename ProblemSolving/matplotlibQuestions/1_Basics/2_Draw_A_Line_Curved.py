# 2. Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 1])

plt.plot(x,y)
plt.title("Sample Graph!")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.show()