# Create two 1D NumPy arrays and perform element-wise addition, subtraction, multiplication, and division.
import numpy as np
array1=np.array([1,2,3,4,5])
array2=np.array([10,20,30,40,50])

print("Addition",np.add(array1,array2))

print("Subtraction",np.subtract(array2,array1))

print("Multiplication",np.multiply(array1,array2))

print("MAX Array1",np.max(array1))

print("MIN Array2",np.min(array2))