# 7. Write a Python programming to display a bar chart of the popularity of programming Languages. Specify the position of each bar plot.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x_position = [i for i, _ in enumerate(languages)]
# y_position = [0,1,2,3,4,5]
y_position = [0,1,4,7,9,10]

plt.title("Popularity of Programming Language\n Worldwide, Oct 2017 compared to a year ago.")
plt.xlabel("x - axes")
plt.ylabel("y - axes")

plt.bar(y_position, popularity)

# plt.xticks(x_position, languages)
plt.xticks(y_position, languages)

plt.minorticks_on()
plt.grid(which="major", color="red", linewidth=0.5, linestyle="-")
plt.grid(which="minor", color="black", linewidth=0.5, linestyle=":")

plt.show()




