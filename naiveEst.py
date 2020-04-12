#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define fixed global variable
h = 2

# Open the data.txt in the current directory
data_file = open("data.txt")

# Extract metadata from data.txt file and convert the values into integer
n, m = list(map(int, data_file.readline().replace('\n','').split(',')))

# Initialise empty dataset
data_list = [] 

# Based on the n in the metadata, read the data from each line and put into list
for i in range(n):
    instance_list = list(map(float,data_file.readline().replace('\n','').split(' ')))
    length = len(instance_list)
    
    # Raise exception if the number of features do not match with m in the metadata
    if (length != m):
        raise Exception("Incorrect number of feature at Line " + str(n) + " of data file. Supposed to have " + str(m) 
                        + " features but there is " + str(length) + " features.")
    data_list.append(instance_list.copy())        

data_file.close()

print("The training data are: ")
print(data_list)

output_file = open("output.txt", "w")

# Assume the testing set is the training set, you may change the list into another training set by replacing data_list.
for num, test_instance_tuple in enumerate(data_list):
    # Compute the number of training set that is within the hypercube of h length with the test data point as center
    count = 0
    
    # Iterate through the training set
    for train_instance_tuple in data_list:
        
        # Test if the distance between each of the test data feature and the training data feature is lesser than h/2
        included = True # Assume that it is lesser than h/2 first
        for i in range(m):
            d = abs(test_instance_tuple[i] - train_instance_tuple[i])
            if (d >= h/2):
                included = False
                break
        
        if (included):
            count += 1
    
    # Compute the probability density function = count / (n * V) where V is h^m
    p = count / (n * h ** m)
    
    # Write into the output file and include newline only when it is not the last entry of the testing data instance
    output_file.write(str(p) + '\n') if num+1 != len(data_list) else output_file.write(str(p))

output_file.close()
print("Output.txt is generated.")


# In[ ]:




