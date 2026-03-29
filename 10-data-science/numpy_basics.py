# NumPy Basics
# Course 4 §Data Science section

import numpy as np

# ═══════════════════════════════════════
#  ARRAY CREATION
# ═══════════════════════════════════════
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2D array (matrix)

print(a)
print(b)
print(f"Shape: {b.shape}")  # (3, 3)
print(f"Dtype: {a.dtype}")  # int64
print(f"Ndim:  {b.ndim}")  # 2
print(f"Size:  {b.size}")  # 9

# Convenience constructors
print(np.zeros((3, 4)))
print(np.ones((2, 3)))
print(np.eye(3))  # identity matrix
print(np.arange(0, 20, 2))  # like range()
print(np.linspace(0, 1, 6))  # 6 evenly spaced values from 0 to 1

# Random arrays
rng = np.random.default_rng(seed=42)
rand = rng.random((3, 3))  # values in [0, 1)
normal = rng.standard_normal(100)  # standard normal distribution
print(rand)

# ═══════════════════════════════════════
#  INDEXING AND SLICING
# ═══════════════════════════════════════
arr = np.arange(12).reshape(3, 4)
print(arr)

print(arr[0])  # first row
print(arr[:, 1])  # second column (all rows)
print(arr[1:, 2:])  # submatrix: rows 1+, cols 2+

# Boolean indexing
data = np.array([5, -3, 8, -1, 2, -7, 4])
print(data[data > 0])  # [5 8 2 4]
data[data < 0] = 0  # replace negatives with 0
print(data)

# ═══════════════════════════════════════
#  MATH OPERATIONS
# ═══════════════════════════════════════
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print(x + y)  # element-wise
print(x * y)
print(x**2)
print(np.sqrt(x))
print(np.dot(x, y))  # dot product: 300

# Broadcasting
matrix = np.ones((3, 4))
row = np.array([1, 2, 3, 4])
print(matrix + row)  # row added to each row of matrix

# ═══════════════════════════════════════
#  STATISTICS
# ═══════════════════════════════════════
scores = np.array([85, 92, 78, 95, 60, 88, 74, 91])

print(f"Mean:   {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")
print(f"Std:    {np.std(scores):.2f}")
print(f"Min:    {np.min(scores)}, Max: {np.max(scores)}")
print(f"25th pct: {np.percentile(scores, 25):.1f}")
print(f"75th pct: {np.percentile(scores, 75):.1f}")

# Axis-wise operations on 2D array
m = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(m, axis=0))  # column sums: [5, 7, 9]
print(np.sum(m, axis=1))  # row sums:    [6, 15]

# ═══════════════════════════════════════
#  LINEAR ALGEBRA
# ═══════════════════════════════════════
A = np.array([[2, 1], [5, 3]])
B = np.array([[1, 0], [0, 1]])

print(np.matmul(A, B))  # matrix multiply
print(np.linalg.det(A))  # determinant
print(np.linalg.inv(A))  # inverse
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)

# --- LAB EXERCISES ---
# 1. Create a 5×5 matrix of random integers (0–100).
#    Find: max per row, min per column, overall mean.
# 2. Normalize a 1D array to [0, 1] range: (x - min) / (max - min)
# 3. Implement matrix multiplication manually with nested loops.
#    Compare result with np.matmul() on a 3×3 matrix.
