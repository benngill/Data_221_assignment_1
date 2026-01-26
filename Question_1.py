#!/usr/bin/env python
# coding: utf-8

# In[3]:


product = 1
currentNumber = 1
threshold = 100 # store threshold value
i = 1

while product <= threshold: # is it better practice to use a while loop that needs an i, or a for loop 
    i = i+1
    product = currentNumber*i
    currentNumber = product # tracks current multiplier
print("FINAL PRODUCT:", product, " OVERFLOW INTEGER:", i) # print final product and overflow integer

