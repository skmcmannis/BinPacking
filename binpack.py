#Uses approximation algorithms to solve the bin packing problem in three ways:
# 1: First Fit
# 2: First Fit Decreasing
# 3: Best Fit
# Input is read from a file named 'bin.txt'
#Author: Shawn McMannis
#Last mod date: 5/30/19


from itertools import islice
import time

#Uses a FIRST-FIT algorithm to determine number of bins needed
def FirstFit(weights, binCap):

    #Number of bins required
    numBins = 0

    #List to store remaining space in each bin
    remainingSpace = [0 for x in range(len(weights))]

    #Iterate through each item in weights[]
    for item in weights:

        #Current bin number
        curBin = 0

        #Iterate through existing bins to see if the item fits
        for bin in range(0, numBins):

            #If the item fits, subtract its weight from remaining weight for that bin
            if remainingSpace[bin] >= item:
                remainingSpace[bin] = remainingSpace[bin] - item
                break
            else:
                curBin = curBin + 1

        #If the item doesn't fit anywhere, open a new bin
        if curBin == numBins:
            remainingSpace[numBins] = binCap - item
            numBins = numBins + 1

    return numBins


#Uses a FIRST-FIT-DECREASING algorithm to determine number of bins needed
def FirstFitDec(weights, binCap):

    #Number of bins required
    numBins = 0

    #List to store the sorted list of weights
    curWeights = []

    #Sort the list of weights into decreasing order
    curWeights = sorted(weights, reverse=True)

    #List to store remaining space in each bin
    remainingSpace = [0 for x in range(len(curWeights))]

    #Iterate through each item in weights[]
    for item in curWeights:

        #Current bin number
        curBin = 0

        #Iterate through existing bins to see if the item fits
        for bin in range(0, numBins):

            #If the item fits, subtract its weight from remaining weight for that bin
            if remainingSpace[bin] >= item:
                remainingSpace[bin] = remainingSpace[bin] - item
                break
            else:
                curBin = curBin + 1

        #If the item doesn't fit anywhere, open a new bin
        if curBin == numBins:
            remainingSpace[numBins] = binCap - item
            numBins = numBins + 1

    return numBins


#Uses a BEST-FIT algorithm to determine number of bins needed
def BestFit(weights, binCap):

    #Number of bins required
    numBins = 0

    #Minimum space left
    minimum = 0

    #Index of target bin
    binIdx = 0

    #List to store remaining space in each bin
    remainingSpace = [0 for x in range(len(weights))]

    #Iterate through each item in weights[]
    for item in weights:

        #Initialize variables for each pass
        minimum = binCap + 1
        binIdx = 0

        #Iterate through existing bins to see if the item fits
        for bin in range(0, numBins):

            #If the item fits, subtract its weight from remaining weight for that bin
            if (remainingSpace[bin] >= item) and ((remainingSpace[bin] - item) < minimum):
                binIdx = bin
                minimum = remainingSpace[bin] - item

        #If the item doesn't fit anywhere, open a new bin
        if minimum == binCap + 1:
            remainingSpace[numBins] = binCap - item
            numBins = numBins + 1
        else:
            remainingSpace[binIdx] = remainingSpace[binIdx] - item

    return numBins


#main

#Number of test cases included in input file
numTests = 0

#Capacity of bins
binCap = 0

#Number of items
numItems = 0

#Weights of each item
weights = []

#Start time
start = 0

#End time
end = 0

#Elapsed time
elapsedTime = 0

#Open import file
with open("bin.txt", "r") as importFile:

    #Set number of tests included in input file
    numTests = list(islice(importFile, 1))
    numTests = int(numTests[0])

    #Iterate through test cases
    for i in range(0, numTests):
        #Get bin capacity
        binCap = list(islice(importFile, 1))
        binCap = int(binCap[0])

        #Get number of items (not used, only here to advance iterator)
        numItems = list(islice(importFile, 1))

        #Get weights of each item
        tempWeights = list(islice(importFile, 1))
        weights = str(tempWeights[0])
        for weight in weights:
            weight = weights.split()
        weights = [int(j) for j in weight]

        print("Test Case", i + 1, end='')

        #Run the FIRST-FIT algorithm
        start = time.perf_counter()
        print(" First Fit:", FirstFit(weights, binCap), end='')
        print(", ", end='')
        end = time.perf_counter()
        elapsedTime = round((end - start) * 1000, 10)
        print(elapsedTime, end='')
        print(".", end='')

        #Run the FIRST-FIT-DECREASING algorithm
        start = time.perf_counter()
        print(" First Fit Decreasing:", FirstFitDec(weights, binCap), end='')
        print(", ", end='')
        end = time.perf_counter()
        elapsedTime = round((end - start) * 1000, 10)
        print(elapsedTime, end='')
        print(".", end='')

        #Run the BEST-FIT algorithm
        start = time.perf_counter()
        print(" Best Fit:", BestFit(weights, binCap), end='')
        print(", ", end='')
        end = time.perf_counter()
        elapsedTime = round((end - start) * 1000, 10)
        print(elapsedTime, end='')
        print(".")