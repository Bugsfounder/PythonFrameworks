# 8. Write a Python programming to display a bar chart of the popularity of programming Languages. Select the width of each bar and their positions.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x_position = [position for position, value in enumerate(languages)]
y_position = [1,3,5,7,9,10]
width = [0.2, 1.1, 2, 0.5, 0.8,1.5]

plt.title("Popularity of Programming Language\n Worldwide, Oct 2017 compared to a year ago.")
plt.xlabel("x - axes")
plt.ylabel("y - axes")
plt.xticks(y_position, languages)
plt.bar(y_position, popularity, width=width, edgecolor='cyan')

plt.minorticks_on()
plt.grid(which="major", color="red", linewidth=0.5, linestyle="-")
plt.grid(which='minor', color="black", linewidth=0.5, linestyle=":")

plt.show()
