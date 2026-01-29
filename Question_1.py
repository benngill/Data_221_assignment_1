product = 1
currentNumber = 1
threshold = 100 # store threshold value
i = 1

while product <= threshold: # loops till threshold is exceeded 
    i = i+1
    product = currentNumber*i
    currentNumber = product # tracks current multiplier
print("FINAL PRODUCT:", product, " OVERFLOW INTEGER:", i) # print final product and overflow integer

