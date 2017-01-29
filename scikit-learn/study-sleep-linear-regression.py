
""" Simple LinearRegression Problem

    We have a student study and sleep data (hour) using these 
    system predict how much mark he will score in the exame 
    """

# from sklearn import linear_model

# #number of hour sleep and study
# feature = [[3, 5], [5, 1], [10, 2]]

# #mark secured
# label = [75, 82, 93]

# reg = linear_model.LinearRegression()
# reg.fit(feature, label)

# result = reg.predict([8, 3])
# print result


from sklearn.linear_model import LinearRegression

#number of hour study
feature = [5, 6, 4, 1, 10]

#mark secured
label = [75, 80, 70, 40, 85]

reg = LinearRegression()
reg.fit(feature, label)

result = reg.predict(3)
print result