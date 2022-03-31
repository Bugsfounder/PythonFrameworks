# 11. Write a Python program to create bar plot from a DataFrame.
# Sample Data Frame:
#   a b c d e
# 2 4,8,5,7,6
# 4 2,3,4,2,6
# 6 4,7,4,7,8
# 8 2,6,4,8,6
# 10 2,4,3,3,2

from turtle import color
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

data = np.array([[4,8,5,7,6],[2,3,4,3,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df = DataFrame(data, columns=("A", "B","C","D","E"), index=[2,4,6,8,10])

df.plot(kind="bar", edgecolor="crimson")

plt.minorticks_on()
plt.grid(which='major', color="green", linewidth=0.5, linestyle="-")
plt.grid(which='minor', color="black", linestyle=":", linewidth=0.5)
plt.show()