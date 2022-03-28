import numpy as np
from sklearn import linear_model

reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, .1])

print(reg.coef_)
print(reg.intercept_)
