# 10. Write a Python program to plot quantities which have an x and y position.

import matplotlib.pylab as plt

x1, y1, x2, y2 = ([2, 3, 5, 6, 8], [1, 5, 10, 18, 20], [3, 4, 6, 7, 9], [2, 6, 11, 20, 22])

plt.axis([0, 10, 0, 30])
plt.plot(x1, y1,"b*" , x2,y2,"ro")
plt.show()
