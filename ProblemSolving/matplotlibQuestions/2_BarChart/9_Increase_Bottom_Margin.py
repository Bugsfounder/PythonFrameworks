# 9. Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

from turtle import color
import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x_position = [i for i, _ in enumerate(languages)]

plt.bar(x_position, popularity)
plt.xticks(x_position, languages, rotation=90)
plt.subplots_adjust(bottom=0.4, top=0.8)
plt.title("Popularity of Programming Language\n Worldwide, Oct 2017 compared to a year ago.")
plt.ylabel("Popularity")
plt.xlabel("Languages")
plt.minorticks_on()
plt.grid(which="major", color='red', linewidth=0.5, linestyle="-")
plt.grid(which="minor", color="black", linestyle=":", linewidth=0.5)
plt.show()
