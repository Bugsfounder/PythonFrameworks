from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

data_x = np.array([[1], [2], [3]])
data_X_train = data_x
data_X_test = data_x

data_y = np.array([3, 2, 4])
data_Y_train = data_y
data_Y_test = data_y

model = linear_model.LinearRegression()
model.fit(data_X_train, data_Y_train)

data_y_predict = model.predict(data_X_test)
squaredError = mean_squared_error(data_Y_test, data_y_predict)

# Printing values
print("Mean Squared Error", squaredError, sep=": ")
print("Weights", model.coef_, sep=": ")  # w1, w2, w3 .... wn
print("Intersept: ", model.intercept_)  # w0 (w not) w!

# Plot the model
plt.scatter(data_Y_test, data_Y_test)
plt.plot(data_X_test, data_y_predict)

plt.show()
