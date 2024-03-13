import numpy as np

#not methods attributes 

# Creating a sample array
arr = np.array([[1, 2.1, 3], ["manvi", 5.0, 6]])

# ndim: Number of dimensions (axes) of the array.
print("Number of dimensions:", arr.ndim)

# shape: Tuple of integers indicating the size of the array in each dimension.
print("Shape of the array:", arr.shape)

# size: Total number of elements in the array.
print("Total number of elements:", arr.size)

# dtype: Data type of the array's elements.
print("Data type of elements:", arr.dtype)

# itemsize: Size in bytes of each element of the array.
print("Size of each element (in bytes):", arr.itemsize)

# nbytes: Total size in bytes of the array's memory.
print("Total size of memory (in bytes):", arr.nbytes)

# strides: Tuple of integers indicating the number of bytes to step in each dimension when traversing the array.
print("Strides of the array:", arr.strides)

# flags: Information about the memory layout and other array properties.
print("Flags of the array:", arr.flags)

# real: Real part of the array if it has complex data type.
print("Real part of the array (if complex):", arr.real)

# imag: Imaginary part of the array if it has complex data type.
print("Imaginary part of the array (if complex):", arr.imag)

# T (or transpose()): Transpose of the array, exchanging rows and columns.
print("Transpose of the array:")
print(arr.T)

# flat: 1-dimensional iterator over the array's elements.
print("1-dimensional iterator over the array's elements:")
for item in arr.flat:
    print(item)

# ctypes: Object for interacting with the array's memory using ctypes.
print("Object for interacting with the array's memory using ctypes:")
print(arr.ctypes)

# Using different ways to access attributes:

# 1. Directly accessing attributes
print("Accessing attributes directly:")
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

# 2. Using getattr() function
print("Using getattr() function:")
print("Size:", getattr(arr, 'size'))

# 3. Using vars() function
#print("Using vars() function:")
#attributes = vars(arr)
#print("Item size:", attributes['itemsize'])
