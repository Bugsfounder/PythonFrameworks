# 13. Write a Python program to create bar plots with errorbars on the same figure. Attach a text label above each bar displaying men means (integer value).
# Sample Data
# Mean velocity:(54.74, 42.35, 67.37, 58.24, 30.25)
# Standard deviation of velocity: (4, 3, 4, 1, 5)

from cgitb import handler
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

n = 5
men = (54.74, 42.35, 67.37, 58.24, 30.25)
men_std= (4, 3, 4, 1, 5)

index = np.arange(n)
width = 0.35

fig, ax = plt.subplots()
graph1 = ax.bar(index, men, width, color="red", yerr=men_std)

plt.ylabel("Scores")
plt.xlabel("Velocity")
plt.title("Scores by Velocity")

red_patch = mpatches.Patch(color='red', label="Men")
plt.legend(handles=[red_patch])

def autoLabel(graphs):
    for graph in graphs:
        height = graph.get_height()
        ax.text(graph.get_x() + graph.get_width()/2., 1.05*height, "%d"% int(height), ha='center', va='bottom')

autoLabel(graph1)
plt.show()
