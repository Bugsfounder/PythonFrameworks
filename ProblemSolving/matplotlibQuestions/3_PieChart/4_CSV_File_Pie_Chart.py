# 4. Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.
# Sample data:
# medal.csv
# country,gold_medal
# United States,46
# Great Britain,27
# China,26
# Russia,19
# Germany,17

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('medal.csv')

country = data['country']
goldMedal = data['gold_medal']
color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

explode = [0 for i in goldMedal]
explode[0] = 0.1

plt.pie(goldMedal, explode=explode, colors=color, labels=country, shadow=True, autopct="%1.1f%%", startangle=180)

plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={"facecolor":'0.80', "pad":5})

plt.show()
