import numpy as np

print("=== Experiment 1: NumPy Array Creation and Operations ===\n")

# 1. Creating NumPy Arrays using np.array()
print("1. Creating arrays using np.array():")
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# 2. Creating arrays using zeros, ones, empty, random
print("\n2. Creating arrays using special functions:")
zeros_arr = np.zeros((3, 3))
print("Zeros array:\n", zeros_arr)

ones_arr = np.ones((2, 4))
print("Ones array:\n", ones_arr)

empty_arr = np.empty((2, 2))
print("Empty array:\n", empty_arr)

random_arr = np.random.random((2, 3))
print("Random array:\n", random_arr)

# 3. Creating arrays using np.arange()
print("\n3. Creating arrays using np.arange():")
range_arr1 = np.arange(10)
print("arange(10):", range_arr1)

range_arr2 = np.arange(2, 10, 2)
print("arange(2, 10, 2):", range_arr2)

# 4. Creating arrays using np.linspace()
print("\n4. Creating arrays using np.linspace():")
lin_arr = np.linspace(0, 10, 5)
print("linspace(0, 10, 5):", lin_arr)

# 5. Checking dimensions
print("\n5. Checking dimensions:")
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("a.ndim:", a.ndim)
print("b.ndim:", b.ndim)
print("c.ndim:", c.ndim)
print("d.ndim:", d.ndim)