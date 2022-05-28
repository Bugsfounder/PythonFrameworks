# 1. Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages = ['Java', "JavaScript", "Python", "C", "C++", "C#", "PHP"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7, 12.5]

x = [lang  for lang, _ in enumerate(languages)]

plt.title("Popularity of Programming Language Worldwide, \nOct 2017 Compare to a year ago")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.bar(x,popularity)
plt.xticks(x, languages)
plt.minorticks_on()
plt.grid(which='major', color="red", linewidth=0.5, linestyle="-")
plt.grid(which='minor', color="black", linewidth=0.5, linestyle=":")
plt.show()

