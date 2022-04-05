# 5. Write a Pandas program to convert a dictionary to a Pandas series.
# Sample Series:
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# Converted series:
# a 100
# b 200
# c 300
# d 400
# e 800
# dtype: int64

import pandas as pd

pyDict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

pdDict = pd.Series(pyDict)
print(pdDict)