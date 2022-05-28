# 4. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.
# Sample data:
# Test Data:
# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
# marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(math_marks, marks_range, label="Math marks", facecolor='red')
plt.scatter(science_marks, marks_range, label="Science marks", facecolor="green")
plt.title("Scatter Plot")
plt.xlabel("Marks Range")
plt.ylabel("Marks Second")
plt.legend()
plt.show()
