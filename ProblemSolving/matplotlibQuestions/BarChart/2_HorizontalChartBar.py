# 2. Write a Python programming to display a horizontal bar chart of the popularity of programming Languages
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

from turtle import color
from matplotlib import pyplot as plt


languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x = [i for i , _ in  enumerate(languages)]

plt.barh(x, popularity, color="green") 
plt.yticks(x , languages)
plt.title("Popularity of Programming Langauges\n Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.minorticks_on()
plt.grid(which="major", color='red', linewidth=0.5)
plt.grid(which="minor", color="black", linewidth=0.5)

plt.show()