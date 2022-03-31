# 14. Write a Python program to create a stacked bar plot with error bars.
# Note: Use bottom to stack the women?s bars on top of the men?s bars.
# Sample Data:
# Means (men) = (22, 30, 35, 35, 26)
# Means (women) = (25, 32, 30, 35, 29)
# Men Standard deviation = (4, 3, 4, 1, 5)
# Women Standard deviation = (3, 5, 2, 3, 3)

from turtle import color
import numpy as np
import matplotlib.pyplot as plt

n = 5
men = (22,30,35,35,26)
women = (25,32,30,35,29)
menStd = (4,3,4,1,5)
womenStd = (3,5,2,3,3)

index = np.arange(n)

width = 0.35

p1 = plt.bar(index, men, width, yerr=menStd, color="red")
p2 = plt.bar(index, womenStd, width, bottom=men, yerr=womenStd, color = 'green')

plt.ylabel('Scores')
plt.xlabel('Groups')
plt.title('Scores by group\n' + 'and gender')
plt.xticks(index, ("Group1", "Group2", "Group3", "Group4", "Group5"))
plt.yticks(np.arange(0,81,10))
plt.legend(("Men", "Women"))
plt.show()