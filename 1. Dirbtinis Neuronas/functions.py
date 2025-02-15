#
import random
import matplotlib.pyplot as plt

#seed that was used for the final project version was 100
random.seed(100)

#generates an array of points around given x and y with a set spread
def generateInputClass(center_x, center_y, spread):
    points = []
    for d in range(0,10):
        x = random.uniform(center_x - spread, center_x + spread)
        y = random.uniform(center_y - spread, center_y + spread)
        points.append((x, y))
    return points
    
#displays a graph from the given generated input sets
def plotInput(givenListOne, givenListTwo):
    x1, y1 = zip(*givenListOne)  
    x2, y2 = zip(*givenListTwo)  

    plt.figure(figsize=(6,6))
    plt.scatter(x1, y1, color='blue', label='Class 1')
    plt.scatter(x2, y2, color='red', label='Class 2')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Input classes")
    plt.legend()
    plt.show()
#genereate final input value(a) from previously generated inputs
def verifyOutput(x1, x2, wMin, wMax, bMin, bMax):
    w1 = random.uniform(wMin, wMax)
    w2 = random.uniform(wMin, wMax)
    b  = random.uniform(bMin, bMax)
    a  = x1 * w1 + x2 * w2 + b
    return a

def threshHoldFunction(a):
    if a >= 0:
        return 1
    else:
        return 0

def sigmoidFunction(a):
    return 1

def neuron(inputClassOne, inputClassTwo, mode, neededCorrectSets):
    selectedWeights = [] # (w1, w2, b)

    wMin = -5
    wMax =  5
    bMin =  -5
    bMax =  5

    while len(selectedWeights) < neededCorrectSets:
        correctly_classified = True
        outputListOne = []
        outputListTwo = []

        w1 = random.uniform(wMin, wMax)
        w2 = random.uniform(wMin, wMax)
        b  = random.uniform(bMin, bMax)

        for (x1,y1), (x2,y2) in zip(inputClassOne, inputClassTwo):
            a1  = x1 * w1 + y1 * w2 + b
            a2  = x2 * w1 + y2 * w2 + b

            #threshHoldFunction
            if mode == 1:
                out1 = threshHoldFunction(a1)
                out2 = threshHoldFunction(a2)
            #threshHoldFunction
            if mode == 2:
                out1 = sigmoidFunction(a1)
                out1 = sigmoidFunction(a2)

            outputListOne.append(out1)
            outputListTwo.append(out2)

        # check if the last output set was valid
        for j in range(len(outputListOne)):
            if outputListOne[j] != 1 or outputListTwo[j] != 0:
                correctly_classified = False
                break

        if correctly_classified:
            selectedWeights.append((w1, w2, b))
            print(w1, w2 , b)
            print(outputListOne)
            print(outputListTwo)

    return selectedWeights
