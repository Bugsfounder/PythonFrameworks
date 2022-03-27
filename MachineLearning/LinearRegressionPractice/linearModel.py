from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [1, 2, 3])
# reg.fit([[1, 2], [4, 8], [3, 7]], [1, 2, 3])

weights = reg.coef_
print(weights)

intercept = reg.intercept_
print(intercept)
