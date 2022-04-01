# 6. Write a Python program to draw a scatter plot to find sea level rise in past 100 years.


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

data = pd.read_csv("data1.csv")

year = data['Year']
# level = data["GMSL"]
level = data["CSIRO Adjusted Sea Level"]

print(year, level)

plt.scatter(year, level, edgecolors='g')
plt.show()