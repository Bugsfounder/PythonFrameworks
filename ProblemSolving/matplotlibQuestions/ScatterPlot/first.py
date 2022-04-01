import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import randn

x, y = [randn(200)],[randn(200)]
x1,y1 = [randn(200)],[randn(200)]

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.scatter(x,y)
# plt.scatter(x,y, facecolor="white", edgecolors='blue')
# plt.scatter(x,y, facecolor="none", edgecolors='blue')
# plt.scatter(x,y , edgecolors='black', s=90)
# plt.scatter(x1,y1, edgecolors='black', s=90)


plt.scatter(math_marks, marks_range, s=100)
plt.scatter(science_marks, marks_range, s=100)


plt.show()