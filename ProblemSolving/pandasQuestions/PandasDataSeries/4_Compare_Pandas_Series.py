# 4. Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd

srs1, srs2 = pd.Series([2,4,6,8,10]), pd.Series([1,3,5,7,10])

print("series1 == series2")
print(srs1==srs2)

print("series1 > series2")
print(srs1>srs2)

print("series1 < series2")
print(srs1<srs2)
