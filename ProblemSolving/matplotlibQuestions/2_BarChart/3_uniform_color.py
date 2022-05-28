'''
3. Write a Python programming to display a bar chart of the popularity of programming Languages. Use uniform color. 
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''
# 0.4, 0.6, 0.8, 1.0

import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x = [i for i, _ in enumerate(languages)]

# plt.bar(x, popularity)
# plt.bar(x, popularity, color='#6698cb')
plt.bar(x, popularity, color=(0.4, 0.6, 0.8, 1.0))
plt.xticks(x, languages)

plt.title("Popularity of Programming Langauges\n Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Popularity")
plt.ylabel("Languages")

plt.minorticks_on()
plt.grid(which="major", color="red", linewidth=0.5)
plt.grid(which="minor", color="black", linewidth=0.5)

plt.show()