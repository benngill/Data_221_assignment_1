def dictOfPercentOfIndicesSmallerThanOrEqualToEachIndex(inputList):
    percentLessOrEqual = {}
    sortedInputList = sorted(inputList) # sorted pre input so that dict is sorted on return
    print(sortedInputList)
    for i in range(0,len(sortedInputList)):
        percentCounter = 0
        for j in range(0,len(sortedInputList)): 
            if sortedInputList[j] <= sortedInputList[i]:
                percentCounter = percentCounter + 1 # tallies number of indices that are <= current index
        percentLessOrEqual[sortedInputList[i]] = percentCounter/len(sortedInputList) # stores each unique value as key, value is % of list that are <= key 
    return percentLessOrEqual

numbers = [3,1,2,3,4,2]
dictOfPercentOfIndicesSmallerThanOrEqualToEachIndex(numbers)