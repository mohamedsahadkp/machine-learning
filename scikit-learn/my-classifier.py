import random

from scipy.spatial import distance
def euc(a, b):
    return distance.euclidean(a, b)

class MYKNN:
    def fit(self, f_train, l_train):
        self.f_train = f_train
        self.l_train = l_train

    def predict(self, f_test):
        prediction = []
        for row in f_test:
            label = self.closest(row)
            prediction.append(label)
        return prediction

    def closest(self, row):
        ecu_dist = euc(row, self.f_train[0])
        best_index = 0
        for i in range(1 , len(self.f_train)):
            dist = euc(row, self.f_train[i])
            if(dist < ecu_dist):
                ecu_dist = dist
                best_index = i
        return self.l_train[best_index] 

from sklearn import datasets
iris = datasets.load_iris()

feature = iris.data
label = iris.target

from sklearn.cross_validation import train_test_split
feature_train, feature_test, label_train, label_test = train_test_split(feature, label, test_size = .5)

# from sklearn import tree
# data = tree.DecisionTreeClassifier()

data = MYKNN()

data.fit(feature_train, label_train)
prediction = data.predict(feature_test)
#print prediction
#print label_test

from sklearn.metrics import accuracy_score
print accuracy_score(label_test, prediction)

