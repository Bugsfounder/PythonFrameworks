from sklearn import linear_model

reg = linear_model.Ridge(alpha=.5)

reg.fit([[0, 0], [1, 1], [2, 2]], [0, .1, 1])

weights = reg.coef_
print(weights)

intercept = reg.intercept_
print(intercept)
