#Slicing in python means taking elements from one given index to another given index.

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])

#Slice elements from index 4 to the end of the array:
print(arr[4:])

#Slice elements from the beginning to index 4 (not included):
print(arr[:4])

#slice elements from reverse order
print(arr[-1])