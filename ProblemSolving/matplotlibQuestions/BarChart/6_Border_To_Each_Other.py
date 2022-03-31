'''
6. Write a Python programming to display a bar chart of the popularity of programming Languages. Make blue border to each bar. Go to the editor
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''


import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.7, 17.6, 8.8, 8, 7.7, 6.7]

x = [index for index, item in enumerate(languages)]

plt.bar(x, popularity, color="#6699cc", edgecolor="blue")
plt.xticks(x, languages)
plt.minorticks_on()
plt.grid(which="major", color="red", linewidth=0.5)
plt.grid(which="minor", color="black", linewidth=0.5)
plt.show()