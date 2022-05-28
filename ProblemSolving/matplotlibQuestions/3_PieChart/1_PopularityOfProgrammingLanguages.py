# 1. Write a Python programming to create a pie chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# The code snippet gives the output shown in the following screenshot:

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = (22.2, 17.6, 8.8, 8, 7.7, 6.7)
color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

explode = (0.1, 0, 0, 0, 0, 0)

plt.pie(popularity, explode=explode, colors=color, labels=languages, shadow=True, autopct="%1.1f%%", startangle=150)    

plt.axis("equal")
plt.show()
