# 10. Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
# Sample Data:
# Means (men) = (22, 30, 35, 35, 26)
# Means (women) = (25, 32, 30, 35, 29)

from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

n_group = 5
men =  (22, 30, 35, 35, 26)
women =  (25, 32, 30, 35, 29)

fig, ax = plt.subplots()

index = np.arange(n_group)

bar_width=0.35
opacity = 0.8

graph1 = ax.bar(index, men, bar_width, alpha=opacity, color="green", label="Men")
graph2 = ax.bar(index+bar_width, women, bar_width, alpha=opacity, color="red", label="Women")

plt.xlabel("Person")
plt.ylabel("Scores")
plt.title("Score by Person")
plt.xticks(index+bar_width, ("G1", "G2", "G3", "G4","G5"))
plt.legend()
plt.show()