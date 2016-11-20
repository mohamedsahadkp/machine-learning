
""" Simple DecisionTreeClassifier machine learning program using iris flower 
    dataset (https://en.wikipedia.org/wiki/Iris_flower_data_set) and draw the decision tree in a pdf """

""" Dependencies
    pip install numpy
    pip install pydotplus
    sudo apt-get install graphviz """

from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()

# print iris.feature_names
# print iris.target_names

# print iris.data[0]
# print iris.target[0]

# for i in range(len(iris.target)):
#     print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])


test_id = [0, 50, 100]

#Test Data
test_target = iris.target[test_id]
test_data = iris.data[test_id]

#Traning Data
traning_target = np.delete(iris.target, test_id)
traning_data = np.delete(iris.data, test_id, axis = 0)

clf = tree.DecisionTreeClassifier()
clf.fit(traning_data, traning_target)

print test_target
print clf.predict(test_data)

#Visualisation 
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         impurity=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_pdf("iris.pdf") 



