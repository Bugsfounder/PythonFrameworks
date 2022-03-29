# Train a logistic regression classifier to predict whether a flower is iris Virginica or not 
from cProfile import label
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()
# print(list(iris.keys()))
# print(iris['data'])
# print(iris['data'].shape)
# print(iris['target'])
# print(iris['DESCR'])

x = iris['data'][:, 3:]
y = (iris['target'] == 2).astype(np.int32)

# Train a Logistic Regression Classifier
clf = linear_model.LogisticRegression()
clf.fit(x,y)

example = clf.predict([[1.6]])
example = clf.predict([[5.6]])
print(example)

# Using Matplotlib to plot the visualization
x_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(x_new)
# print(x_new)
# plt.plot(x_new, y_prob)
plt.plot(x_new, y_prob[:, 1], "g-", label="Virginica")
plt.legend()
plt.show()

