# Waterbottle and Cup

# Different Waterbottle and Cup
# hieght, 

from sklearn.naive_bayes import GaussianNB

feature_data = [[200, 8, 0], [700, 25, 1], [150, 10, 0], [210, 7, 0], [500, 20, 1]]
label_data = [1, 2, 1, 1, 2]

clf = GaussianNB()
clf.fit(feature_data, label_data)

print clf.predict([600, 30, 0])
