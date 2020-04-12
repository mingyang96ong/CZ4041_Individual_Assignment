#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# Define fixed global variable 
h = 2

# Load the training data into data.txt
training_data = np.loadtxt('data.txt', skiprows = 1)

# Get the number of training data and number of feature
n, m = training_data.shape 

print("The training data are: ")
print(training_data)
print()

# As we assumed the testing set is the training set, you may load your own testing data here.
testing_data = training_data.copy()

print("The testing data are: ")
print(testing_data)
print()

output_file = open("output.txt", "w")

for index, testing_instance in enumerate(testing_data):
    count = np.sum(np.all(np.less(np.absolute(training_data - testing_instance), h/2), axis = -1))

    # Compute the probability density function = count / (n * V) where V is h^m
    p = count / (n * h ** m)
    
    # Write into the output file and include newline only when it is not the last entry of the testing data instance
    output_file.write(str(p) + '\n') if index+1 != len(training_data) else output_file.write(str(p))

output_file.close()
print("Output.txt is generated.")


# In[ ]:




