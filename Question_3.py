def twoVariableListToExponentCalculator(inputList):
    exponentMathResult = []
    for i in range(0,len(inputList)): # unpacks input using for loop
        baseX = inputList[i][0]
        exponentY = inputList[i][1]
        if exponentY >= 0: # skips pair if exponent is negative
            exponentMathResult.append(baseX**exponentY) # stores valid results
    return exponentMathResult

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

twoVariableListToExponentCalculator(pairs)