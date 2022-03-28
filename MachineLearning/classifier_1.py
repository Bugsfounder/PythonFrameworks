# Loading Required Moduels
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading Dataset
iris = datasets.load_iris()

# Printing Description
# print(iris.DESCR)

# Describing Features and Labels
features = iris.data
labels = iris.target

# Training the Classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

# Predicting Model
# Setosa       --> 0
# Versicolour  --> 1
# Virginica    --> 2
predict = clf.predict([[1, 1, 1, 1]])  # [0] --> Setosa
predict = clf.predict([[0.2, 1, 4, 3]])  # [1] --> Versicolour
predict = clf.predict([[1, 3, 54, 1]])  # [2]  --> Virginica
predict = clf.predict([[23, 3, 54, 34]])  # [2] --> Virginica

print(predict)
