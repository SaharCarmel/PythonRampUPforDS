# NumPy Introduction
# %%
import numpy as np 

# NumPy arrays are faster and more efficient than regular Python lists for numerical data.

#%%
# Creating arrays
array1 = np.array([1, 2, 3]) # Create a 1D array
print(array1)

array2 = np.array([[1, 2, 3], [4, 5, 6]]) # Create a 2D array
print(array2) 

#%%
# NumPy arrays have attributes like shape, dtype, etc

# Array attributes
print(array2.shape) # Shape is (num_rows, num_cols) 
print(array2.dtype) # Data type of array elements

#%%
# Arithmetic operations are vectorized in NumPy

arr1 = np.array([1, 2, 3])  
arr2 = np.array([4, 5, 6])

print(arr1 + arr2) # Element-wise addition  
print(arr1 * arr2) # Element-wise multiplication

#%%
# Lots of built-in math/statistics functions

arr = np.array([1, 6, 20])  

print(np.abs(arr)) # Absolute value  
print(np.sqrt(arr)) # Element-wise square root

#%%
# Indexing and slicing like Python lists

mat = np.array([[1,2], [3,4], [5,6]]) 

print(mat[0, 1]) # Index row 0, column 1
print(mat[0:2, 1]) # Slice rows 0 and 1, column 1

#%%
# Useful functions for creating arrays

arr = np.linspace(0, 10, 5) # Evenly spaced values 
print(arr)

random_arr = np.random.rand(2, 3) # Random values
print(random_arr)  

#%%
# Aggregate functions

stats_arr = np.array([[1,2,3], [4,5,6]])

print(stats_arr.sum())  
print(stats_arr.mean())
print(stats_arr.std()) # Standard deviation
# %%
