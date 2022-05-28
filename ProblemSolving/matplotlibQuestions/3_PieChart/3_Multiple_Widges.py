# 3. Write a Python programming to create a pie chart with a title of the popularity of programming Languages.Make multiple wedges of the pie.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

explode = [0.1, 0, 0, 0, 0, 0]

plt.pie(popularity, explode=explode, colors=color, labels=languages, shadow=True, autopct="%1.1f%%", startangle=140)

plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={"facecolor":"0.8", 'pad':5})

plt.show()




