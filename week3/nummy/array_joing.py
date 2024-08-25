import numpy as  np
array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8])
array3=np.concat((array1,array2))
print(array3)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
print(np.concat((arr1,arr2),axis=1))