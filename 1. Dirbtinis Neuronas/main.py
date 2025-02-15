#Author: Simonas Jaunius Urbutis
#Project: Simulating a neuron model working principles
#Summary: The code generates a cluster of 2D points that are divided into two classes by generating a linear function.
#         The neuron finds the weights for the target function by brute forcing and seeing if the classes correctly match.
import functions
import matplotlib.pyplot as plt

#Generate input points
inputClassOne = functions.generateInputClass(center_x=-2, center_y=-2, spread=5)
inputClassTwo = functions.generateInputClass(center_x=5, center_y=5, spread=5)

# Check the generated input points
#print(inputClassOne)
#print(inputClassTwo)

#Plot the generated input points
functions.plotInput(inputClassOne, inputClassTwo)

#Neuron activation from generated points
outputListThreshold, iterationsThreshold = functions.neuron(inputClassOne, inputClassTwo, 1, 3)
outputListSigmoid, iterationsSigmoid = functions.neuron(inputClassOne, inputClassTwo, 2, 3)

# Check the generated weight lists
#print(outputListSigmoid)
#print(outputListThreshold)

#Plot the input points and the seperating lines from the found weights
functions.plotInputAndDecisionBoundaries(inputClassOne, inputClassTwo, outputListThreshold)

#TESTING
# print("Threshold function verification:")
# print("Iterations it took: " , iterationsThreshold)
# for w1, w2, b in outputListThreshold:
#     verifyOutput = functions.verifyOutput(inputClassOne, w1, w2, b, 1)
#     print("Class one output:")
#     print(verifyOutput)

#     print("Class two output:")
#     verifyOutput = functions.verifyOutput(inputClassTwo, w1, w2, b, 1)
#     print(verifyOutput)

# print("Sigmoid function verification:")
# print("Iterations it took: " , iterationsSigmoid)
# for w1, w2, b in outputListSigmoid:
#     verifyOutput = functions.verifyOutput(inputClassOne, w1, w2, b, 2)
#     print("Class one output:")
#     print(verifyOutput)

#     verifyOutput = functions.verifyOutput(inputClassTwo, w1, w2, b, 2)
#     print("Class two output:")
#     print(verifyOutput)