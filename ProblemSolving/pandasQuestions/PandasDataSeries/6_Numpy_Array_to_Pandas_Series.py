# 6. Write a Pandas program to convert a NumPy array to a Pandas series.
# Sample Series:
# NumPy array:
# [10 20 30 40 50]
# Converted Pandas series:
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50
# dtype: int64

import pandas as pd
import numpy as np

npArr = np.array([10,20,30,40,50])

pdArr = pd.Series(npArr)
print(pdArr)