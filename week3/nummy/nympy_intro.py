#NumPhy -> Python library used for working with arrays. 50X faster than arrays

import numpy as np
arr =np.array([1,2,3,4,5])
print(arr)
#print array dimension
twodimension_arr=np.array([[1,2,3,4],[5,6,7,8]])
threedim_array=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Single Dimension",arr.ndim)
print("Two Dimension",twodimension_arr.ndim)
print("Three Dimension",threedim_array.ndim)

higherdim_arr=np.array([1,2,3],ndmin=5)

print("Higher Dimension",higherdim_arr.ndim)





