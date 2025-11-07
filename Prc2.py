import numpy as np

print("=== Experiment 2: NumPy Array Functions ===\n")

# 1. Array Indexing
print("1. Array Indexing:")
arr = np.array([1, 2, 3, 4])
print("Array:", arr)
print("arr[0]:", arr[0])

# 2. 2D Array Indexing
print("\n2. 2D Array Indexing:")
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2D Array:\n", arr_2d)
print("2nd element on 1st row (arr[0, 1]):", arr_2d[0, 1])

# 3. Array Slicing
print("\n3. Array Slicing:")
arr_slice = np.array([1, 2, 3, 4, 5, 6, 7])
print("Array:", arr_slice)
print("arr[1:5]:", arr_slice[1:5])
print("arr[::2]:", arr_slice[::2])
print("arr[3:]:", arr_slice[3:])

# 4. Getting Array Shape
print("\n4. Array Shape:")
shape_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Array:\n", shape_arr)
print("Array shape:", shape_arr.shape)

# 5. Reshaping Arrays
print("\n5. Reshaping Arrays:")
reshape_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original array:", reshape_arr)
newarr = reshape_arr.reshape(4, 3)
print("Reshaped to (4, 3):\n", newarr)

# 6. Additional Operations
print("\n6. Additional Operations:")
# Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array a:", a)
print("Array b:", b)
print("a + b:", a + b)
print("a * b:", a * b)

# Statistical operations
stats_arr = np.array([1, 2, 3, 4, 5])
print("\nStatistical operations on", stats_arr)
print("Mean:", np.mean(stats_arr))
print("Max:", np.max(stats_arr))
print("Min:", np.min(stats_arr))
print("Sum:", np.sum(stats_arr))