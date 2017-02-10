
from __future__ import division
from numpy import *

def findError(b, m, trainigData):
    totalError = 0
    for i in range(0, len(trainigData)):
        x = trainigData[i, 0]
        y = trainigData[i, 1]
        totalError += ((y - (m * x + b)) ** 2)
        print totalError

    return totalError / float(len(trainigData))

def gradientDecsent(initalYIntercept, initalSlop, numberOfIteration, learingRate, trainigData):
    m = initalSlop
    b = initalYIntercept

    for i in range(numberOfIteration):
        # Update b and m with new accurate value
        m, b = gradientDecsentSteps(m, b, learingRate, array(trainigData))

    return [m, b]

def gradientDecsentSteps(m , b, learingRate, trainigData):

    mGradient = 0
    bGradient = 0
    numberOfTrainingData = len(trainigData)
    N = float(numberOfTrainingData)
    for i in range(0, numberOfTrainingData):
        x = trainigData[i, 0]
        y = trainigData[i, 1]

        mGradient += - ((2 / N) * x * (y - ((m * x) + b)))
        bGradient += - ((2 / N) * (y - (m * x + b)))

    newMGradient = m - (learingRate * mGradient)
    newBGradient = b - (learingRate * bGradient)
    return [newMGradient, newBGradient]
        
def run():
    #Step 1 : Read trainig data
    trainigData = genfromtxt('../resource/data/student-study-mark.csv', delimiter=",")

    #Step 2 : Define hyperparameter
    learingRate = 0.0001
    numberOfIteration = 1000
    
    #b
    initalYIntercept = 0
    #m
    initalSlop = 0

    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initalYIntercept, initalSlop, findError(initalYIntercept, initalSlop, trainigData))
    print "Running..."
    [b, m] = gradientDecsent(initalYIntercept, initalSlop, numberOfIteration, learingRate, trainigData)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(numberOfIteration, b, m, findError(b, m, trainigData))

if __name__ == '__main__':
    run()

