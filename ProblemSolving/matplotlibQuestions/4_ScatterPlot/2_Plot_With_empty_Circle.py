# 2. Write a Python program to draw a scatter plot with empty circles taking a random distribution in X and Y and plotted against each other


import matplotlib.pyplot as plt
from matplotlib.pylab import randn

x = randn(200)
y = randn(200)

plt.scatter(x, y, facecolor="none", edgecolors='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()