# 12. Write a Python program to create multiple types of charts (a simple curve and plot some quantities) on a single set of axes.
import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [
    (DT.datetime.strptime("2022-03-30", "%Y-%m-%d"), 772.559998),
    (DT.datetime.strptime("2022-04-01", "%Y-%m-%d"), 776.429993),
    (DT.datetime.strptime("2022-04-02", "%Y-%m-%d"), 776.469971),
    (DT.datetime.strptime("2022-04-03", "%Y-%m-%d"), 776.859985),
    (DT.datetime.strptime("2022-04-04", "%Y-%m-%d"), 775.080017)
]

x, y = [date2num(date) for (date, value ) in data], [value for (date, value) in data]

fig = plt.figure()
graph = fig.add_subplot(111)

graph.plot(x,y,'r-o')
graph.set_xticks(x)
graph.set_xticklabels([date.strftime("%Y-%m-%d") for (date, value) in data])

plt.show()


