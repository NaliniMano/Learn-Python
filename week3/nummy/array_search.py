import numpy as np
arr=np.array([1,2,3,4,2,3,9])
print(np.where(arr==2)) # print the matching index

#Find the indexes where the values are odd:
print(np.where(arr%2!=0))