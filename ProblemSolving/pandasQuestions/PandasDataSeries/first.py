import pandas as pd

pdArr = pd.Series([1,2,3,4,5])

# print(pdArr)
# print(type(pdArr))
# print(type(list(pdArr)))

a = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

am = pd.Series(a)
print(am)