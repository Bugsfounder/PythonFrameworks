# 12. Write a Python program to create bar plots with error bars on the same figure.
# Sample Date
# Mean velocity: 54.74, 42.35, 67.37, 58.24, 30.25
# Standard deviation of velocity: 4, 3, 4, 1, 5

import matplotlib.pyplot as plt
import numpy as np

men =  (54.74, 42.35, 67.37, 58.24, 30.25)
standardMen = (4,3,4,1,5)
n = 5
width = 0.35
index = np.arange(n)

plt.bar(index, men, width=width, yerr=standardMen, color='red')
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')
plt.minorticks_on()
plt.grid(which='major', color="red", linewidth=0.5, linestyle="-")
plt.grid(which='minor', color="black", linewidth=0.5, linestyle=":")
plt.show()
