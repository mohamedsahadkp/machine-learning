# Hello World Machine Learning Programe

""" Here we defined some apple and orange feature.
    Using DecisionTreeClassifier we trained the identified features and labels.
    When we a give new feature to system whch is not trained, The system will predict it the correct label (apple or orange) """

""" features are weight,texture 
    label are apple, orange """
 
from sklearn import tree
#features = [[140, "smooth"], [130, "smooth"], [150,"bumpy"], [170, "bumby"]]
#labels = ["apple", "apple", "orange", "orange"]

#smooth = 0, bumpy = 1
#apple = 0, orange = 1

features = [[140, 0], [130, 0], [150, 1], [170, 1]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[150, 0]])