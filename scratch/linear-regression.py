


import numpy from *


def findError(b, m, trainigData):
    totalError = 0
    for i in range(0, len(trainigData)):
        x = trainigData[i, 0]
        y = trainigData[i, 1]
        totalError += (y - ((m * x) +b) **2
    return totalError / float(len(trainigData))

def gradientDecsent(initalYIntercept, initalSlop, numberOfIteration, learingRate, trainigData):
    m = initalSlop
    b = initalYIntercept

    for i in range(numberOfIteration):
        # Update b and m with new accurate value
        m, b = gradientDecsentSteps(m, b, learingRate, array(trainigData))

    return [m, b]

def gradientDecsentSteps(m , b, learingRate, trainigData):

    initalM = 0
    initalB = 0
    for i in range(0, len(trainigData)):
        



def run():
    #Step 1 : Read trainig data
    trainigData = genfromtxt('data.csv', delimeter=",")

    #Step 2 : Define hyperparameter

    learingRate = 0.001
    numberOfIteration = 1000
    
    #b
    initalYIntercept = 0
    #m
    initalSlop = 0
   








if __name__ == ___main___:
    run(): 

