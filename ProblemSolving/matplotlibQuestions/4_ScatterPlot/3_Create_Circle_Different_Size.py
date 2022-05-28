# 3. Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes. 

import matplotlib.pyplot as plt
import random
import math

numOfBalls = 30
x = [random.triangular() for i in range(numOfBalls)]
y = [random.gauss(0.5, 0.25) for i in range(numOfBalls)]
colors = [random.randint(1,5) for i in range(numOfBalls)]
area = [math.pi*random.randint(1,15)**2 for i in range(numOfBalls)]

# print(x,y,colors,area)
plt.figure()
plt.scatter(x, y, s=area, c=colors)
plt.show()
