# Defining the list
list1 = [2, 51, 11, 13, 51, 100]

# 1. Output every item from list with positive indexing
print("Positive indexing:")
for i in range(len(list1)):
    print(f"Index {i}: {list1[i]}")

# 2. Output every item from list with negative indexing
print("\nNegative indexing:")
for i in range(-1, -len(list1)-1, -1):
    print(f"Index {i}: {list1[i]}")

# 3. Replace the last element of a list with a new value
list1[-1] = 200
print("\nList after replacing the last element:", list1)

# 4. Replace the fifth element of a list with a new value
list1[4] = 150
print("\nList after replacing the fifth element:", list1)
