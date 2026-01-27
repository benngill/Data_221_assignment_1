from random import random

values = [random() for i in range(20)]
x = random()

largerValues = []
exactMatch = None
valuesSorted = sorted(values) # sorts the list
for i in range(20):
    if valuesSorted[i] >= x: # finds indices where list value >= x
        if valuesSorted[i] == x:
            exactMatch = i # stores index of exact match (if applicable)
        largerValues.append(values[i])

print(valuesSorted, "x:",x, "Exact Match is index:", exactMatch) # prints sorted list, value of x, matching index