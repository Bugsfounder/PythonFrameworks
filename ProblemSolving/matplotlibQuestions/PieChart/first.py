import matplotlib.pyplot as plt

plt.pie([1,2,3,4,5], (0.1,0,0,0,0), ("A","B","C","D","E"), ("red", "green", "blue","pink", "yellow"), autopct='%1.1f%%', shadow=True, startangle=40)

# plt.xlabel("This is x")
# plt.ylabel("This is y")
plt.title("Pie Chart")

# plt.minorticks_on()
# plt.grid(which="major", color="red", linewidth=0.5)
# plt.grid(which="minor", color="red", linewidth=0.5)

plt.axis('equal')
plt.show()