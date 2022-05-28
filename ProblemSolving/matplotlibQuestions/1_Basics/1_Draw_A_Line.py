# 1. Write a Python program to draw a line with suitable label in the x axis, y axis and a title. 

import matplotlib.pyplot as plt

x = range(1,50)
y = [value *3 for value in x]

plt.plot(x, y)
plt.title("Draw a line")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
