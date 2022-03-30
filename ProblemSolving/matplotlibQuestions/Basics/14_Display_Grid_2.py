# 14. Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with rendering with a larger grid (major grid) and a smaller grid (minor grid).Turn on the grid but turn off ticks.

import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [
    (DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
    (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
    (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
    (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
    (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )
]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)
graph.plot(x,y, "r-o")

graph.set_xticks(x)
graph.set_xticklabels([date.strftime("%Y-%m-%d") for (date, value) in data])

plt.xlabel("Date")
plt.ylabel("Closing Value")
plt.title("Closign Stock value of Alphabet Inc.")

plt.minorticks_on()
plt.grid(which="major",linestyle="-", linewidth="0.5", color="blue")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

# Turn off the display of all ticks.
plt.tick_params(which='both', # Options for both major and minor ticks
                top='off', # turn off top ticks
                left='off', # turn off left ticks
                right='off',  # turn off right ticks
                bottom='off') # turn off bottom ticks

plt.show()