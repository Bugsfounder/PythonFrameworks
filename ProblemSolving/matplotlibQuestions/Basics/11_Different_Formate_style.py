# 11. Write a Python program to plot several lines with different format styles in one command using arrays.
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t,t, "g--", t, t**2, "s", t,t**3, "^")
plt.show()