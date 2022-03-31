# 17. Write a Python program to add textures (black and white) to bars and wedges. Go to the editor
# Note: Use bottom to stack the women bars on top of the mens bars.

import matplotlib.pyplot as plt

fig = plt.figure()

pattern = ["|", "\\", "/", "+", "-", "*", "X", "o", "O"]
color = ["red", "blue", "black","white", "cyan", "crimson", "yellow", "brown", "purple"]

ax = fig.add_subplot(111)
for i in range(len(pattern)):
    # ax.bar(i, 3, color="white", edgecolor="black", hatch=pattern[i])
    # ax.bar(i, i, color="blue", edgecolor="black", hatch=pattern[i])
    ax.bar(i+1, i, color=color[i], edgecolor="black", hatch=pattern[i])

plt.show()
