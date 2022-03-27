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

# features for model
diabetes_X = diabetes.data

# TrainData and TestData
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[:30]
diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[:30]

# Initializing LinearRegression Using linear_model
model = linear_model.LinearRegression()

# Fitting Data to model
model.fit(diabetes_X_train, diabetes_Y_train)

# Predicted values
diabetes_Y_predict = model.predict(diabetes_X_test)

# Getting Mean Squared Error
squaredError = mean_squared_error(diabetes_Y_test, diabetes_Y_predict)

# Printing values
print("Mean Squared Error", squaredError, sep=": ")
print("Weights", model.coef_, sep=": ")  # w1, w2, w3 .... wn
print("Intersept: ", model.intercept_)  # w0 (w not) w!

# Plot the model
plt.plot(diabetes_X_test, diabetes_Y_predict)

plt.show()
