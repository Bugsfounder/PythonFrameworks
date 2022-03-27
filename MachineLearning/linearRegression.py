import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# Loading Dataset 
diabetes = datasets.load_diabetes()

# Watching Dataset
# print(diabetes)
# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print("Data", diabetes.data, sep=": ")
# print("Target", diabetes.target, sep=": ")
# print("Frame", diabetes.frame, sep=": ")
# print("DESCR", diabetes.DESCR, sep=": ")
# print("Feature_names", diabetes.feature_names, sep=": ")
# print("Data_filename", diabetes.data_filename, sep=": ")
# print("Target_filename", diabetes.target_filename, sep=": ")

diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[:30]

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[:30]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_Y_train)

diabetes_Y_predict = model.predict(diabetes_X_test)

squaredError = mean_squared_error(diabetes_Y_test, diabetes_Y_predict)

print("Mean Squared Error", squaredError, sep=": ")
print("Weights", model.coef_, sep=": ")
print("Intersept: ", model.intercept_)

plt.scatter(diabetes_X_test, diabetes_Y_test)
plt.plot(diabetes_X_test, diabetes_Y_predict)

plt.show()
