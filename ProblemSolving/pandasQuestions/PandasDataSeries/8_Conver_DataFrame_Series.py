# 8. Write a Pandas program to convert the first column of a DataFrame as a Series.
# Sample Output:
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 2 5 5
# 2 3 6 8
# 3 4 9 12
# 4 7 5 1
# 5 11 0 11
# 1st column as a Series:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 7
# 5 11
# Name: col1, dtype: int64
# <class 'pandas.core.series.Series'>

# col1 col2 col3
# 0 1 4 7
# 1 2 5 5
# 2 3 6 8
# 3 4 9 12
# 4 7 5 1
# 5 11 0 11

import pandas as pd

d = {'col1':[0,1,4,7], "col2":[1,2,5,5], "col3":[2,3,6,8], "col4":[3,4,9,12], "col5":[4,7,5,1], "col6":[5,11,0,11]}

df = pd.DataFrame(d)
dfCol1 = df.loc[:, ['col1']]

dfSrs = df.i
print(dfSrs)



