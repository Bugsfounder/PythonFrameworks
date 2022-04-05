# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd
srs1, srs2 = pd.Series([2,4,6,8,10]), pd.Series([1,3,5,7,9])

print("******* Addition *******")
print(f"{srs1+srs2}")

print("******* Substraction *******")
print(f"{srs1-srs2}")

print("******* Multiplication *******")
print(srs1*srs2)

print("******* Division *******")
print(srs1/srs2)
