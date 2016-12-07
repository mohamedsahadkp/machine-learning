
""" Test accuracy of classifer using test and train data (We used iris datasets.
    Iris dataset is flower dataset, ref : https://en.wikipedia.org/wiki/Iris_flower_data_set) 
    We used KNeighborsClassifier algorithm for classification. """

from __future__ import division
from sklearn import datasets
from sklearn.metrics import accuracy_score
iris = datasets.load_iris()

feature = iris.data
label = iris.target
    
from sklearn.cross_validation import train_test_split
feature_train, feature_test, label_train, label_test = train_test_split(feature, label, test_size = .5)

# KNeighbors Algorithm
from sklearn.neighbors import KNeighborsClassifier
data = KNeighborsClassifier()

data.fit(feature_train, label_train)

prediction = data.predict(feature_test)

print accuracy_score(label_test, prediction)

