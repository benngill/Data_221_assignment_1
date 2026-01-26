def dictOfListLength(inputList):
    lengthOfListIndices = {}
    for i in range(0,len(inputList)):
        lengthOfKey = len(inputList[i]) # stores length of string i 
        parity = "odd"
        if lengthOfKey % 2 == 0: # switches parity to 'odd' if string is odd
            parity = "even"
        lengthOfListIndices[inputList[i]] = {"length":lengthOfKey, "parity": parity} # stores each string as a key with length info as value
    return lengthOfListIndices

foodsTest = ["apple", "orange", "banana", "grape"]

dictOfListLength(foodsTest)