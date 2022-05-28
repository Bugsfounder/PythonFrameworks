'''
4. Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x = [index for index, value in enumerate(languages)]

plt.bar(x, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xticks(x, languages)

plt.title("Popularity of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Popularity")
plt.xlabel("Languages")

plt.minorticks_on()
plt.grid(which="major", color="red", linewidth=0.5)
plt.grid(which="minor", color="black", linewidth=0.5)

plt.show()