# 3. Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.

import matplotlib.pyplot as plt

with open('test.txt') as f:
    data = f.read()

data = data.split('\n')

x = [int(line.split(" ")[0]) for line in data]
y = [int(line.split(" ")[1]) for line in data]

print(x,y)

plt.plot(x,y)
# plt.plot([1,2,3],[2,4,1])
plt.title("Sample Graph!")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.show()