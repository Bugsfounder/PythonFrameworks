# 4. Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fdata.csv', sep=",", parse_dates=True, index_col=0)

df.plot()
plt.show()