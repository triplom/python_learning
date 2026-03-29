# Lists
# Course 2 §4 · Course 4 §8

# --- Creation ---
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []
nested = [[1, 2], [3, 4], [5, 6]]

# --- Indexing and slicing ---
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])  # apple
print(fruits[-1])  # elderberry
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[::-1])  # reversed

# --- Mutation ---
fruits[0] = "avocado"
print(fruits)

# --- List methods ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.append(7)  # add to end
nums.insert(0, 0)  # insert at index
nums.remove(1)  # remove first occurrence of value
popped = nums.pop()  # remove and return last element
popped_i = nums.pop(2)  # remove and return at index
nums.sort()  # sort in place
nums.reverse()  # reverse in place
print(nums)
print(nums.index(5))  # find index of value
print(nums.count(1))  # count occurrences
print(len(nums))  # length

# --- Copying (important!) ---
original = [1, 2, 3]
shallow_copy = original.copy()  # or original[:]
shallow_copy.append(4)
print(original)  # [1, 2, 3] — not affected
print(shallow_copy)

# --- List functions ---
data = [3, 1, 4, 1, 5, 9]
print(sum(data))  # 23
print(min(data))  # 1
print(max(data))  # 9
print(sorted(data))  # new sorted list (original unchanged)

# --- Checking membership ---
print("apple" in fruits)  # True
print("grape" not in fruits)  # True

# --- Iterating ---
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# --- Nested lists ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# --- LAB EXERCISES ---
# 1. Create a list of 5 student names. Sort, reverse, and print.
# 2. Remove all duplicates from [1, 2, 2, 3, 3, 3, 4] without using set().
# 3. Given scores = [85, 92, 78, 95, 60, 88], print average, highest, lowest.
# 4. Flatten [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6] without imports.
