# 5. Write a Python programming to display a bar chart of the popularity of programming Languages. Attach a text label above each bar displaying its popularity (float value).
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

def autoLabel(rectangles):
    for rectangle in rectangles:
        height = rectangle.get_height()
        ax.text(rectangle.get_x() + rectangle.get_width()/2., 1.05*height, '%f' % float(height), ha="center", va="bottom")


languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x = [index for index, value in enumerate(languages)]

fig, ax = plt.subplots()
a = ax.bar(x, popularity)

plt.title("Popularity of Programming Languages\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Popularity")
plt.xlabel("Languages")

plt.minorticks_on()
plt.grid(which="major", color="red", linewidth=0.5)
plt.grid(which="minor", color="black", linewidth=0.5)

autoLabel(a)
plt.show()

