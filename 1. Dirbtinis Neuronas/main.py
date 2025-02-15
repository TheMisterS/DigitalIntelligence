import functions
import matplotlib.pyplot as plt

inputClassOne = functions.generateInputClass(2, 2, 1)
inputClassTwo = functions.generateInputClass(5, 5, 1)


print(inputClassOne)
print(inputClassTwo)

# functions.plotInput(inputClassOne, inputClassTwo)

outputList = functions.neuron(inputClassOne, inputClassTwo, 1, 3)
print(outputList)