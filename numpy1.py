import numpy as np

# 1. Converting a list to an array using np.array()
# This method is flexible and can handle different data types within the list.
#it i an entity not method coz () not required 

data_list = [1, 2, 3, 4, 5.6]
array_from_list = np.array(data_list)
print("Array from list:", array_from_list)  # Output: Array from list: [1 2 3 4 5]

# 2. Creating an array of zeros using np.zeros()
# Specify the shape (dimensions) of the desired array.

zeros_array = np.zeros((5, 4))  # Create a 3x4 array filled with zeros
print("Array of zeros:", zeros_array)  # Output: Array of zeros: [[0. 0. 0. 0.]
                                       #                        [0. 0. 0. 0.]
                                       #                        [0. 0. 0. 0.]]

# 3. Creating an array of ones using np.ones()
# Similar to zeros, but fills the array with ones.

ones_array = np.ones((2, 9))
print("Array of ones:", ones_array)  # Output: Array of ones: [[1. 1.]
                                       #                       [1. 1.]]

# 4. Creating an uninitialized array using np.empty()
# This method is faster than zeros or ones but requires explicit assignment later.

empty_array = np.empty((2, 3))
print("Empty array (before assignment):", empty_array)  # Output: Empty array (before assignment): [[1.11022302e-16 1.11022302e-16 1.11022302e-16]
                                                           #                          [1.11022302e-16 1.11022302e-16 1.11022302e-16]]
                                                           # (Elements may vary due to randomness)

# Assign values to the empty array (example)
empty_array[:] = 19.5  # Assign 10 to all elements
print("Empty array (after assignment):", empty_array)  # Output: Empty array (after assignment): [[10. 10. 10.]
                                                           #                                  [10. 10. 10.]]

# 5. Creating an array with evenly spaced values using np.arange()
# Define start, stop (exclusive), and step values.

arange_array = np.arange(10, 29, 2)  # Create an array from 10 to 19 (excluding 20) with step 2
print("Array with arange():", arange_array)  # Output: Array with arange(): [10 12 14 16 18]

# 6. Creating an array with a specified number of evenly spaced values using np.linspace()
# Define start, stop, and the number of elements.

linspace_array = np.linspace(0, 1, 7)  # Create 5 values between 0 (inclusive) and 1 (inclusive)
print("Array with linspace():", linspace_array)  # Output: Array with linspace(): [0.         0.25       0.5        0.75       1.        ]
