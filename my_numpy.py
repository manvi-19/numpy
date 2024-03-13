import numpy as np
#create array
array1 = np.array([1,2,3])
array2 = np.array([[2,3,4],[5,6,7]])
#.size,.shape,.ndim,.sum,.mean

#**.size**: This attribute returns the total number of elements in the array. It's essentially the product of the array's dimensions. For example:

print(array1.size) 
print(array2.size)  

#2. **.shape**: This attribute returns a tuple representing the shape of the array. The shape is a tuple of integers indicating the size of the array in each dimension. For example
    
print(array1.shape)  
print(array2.shape) 
    
#3. **.ndim**: This attribute returns the number of dimensions of the array. For example:

print(array1.ndim) 
print(array2.ndim) 

#4. **.sum()**: This method returns the sum of all elements in the array or along a specified axis. For example:

print(array1.sum())
print(array2.sum())  

#5. **.mean()**: This method computes the arithmetic mean along the specified axis. It returns the average of the array elements. For example:

print(array1.mean())  
print(array2.mean())  
    