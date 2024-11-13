# 1. Pop (მეექვსე ელემენტი ინდექსით)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
popped_item = my_list.pop(5)
print("List after pop:", my_list)
print("Popped item:", popped_item)

# 2. Remove (მეორე ელემენტი მნიშვნელობით)
my_list = [1, 2, 3, 4, 5]
my_list.remove(2)
print("List after remove:", my_list)

# 3. Append (დაამატე ახალი ელემენტი ბოლოში)
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("List after append:", my_list)

# 4. Insert (ჩაამატე ახალი ელემენტი კონკრეტულ ინდექსზე)
my_list = [1, 2, 3, 4, 5]
my_list.insert(1, 9)
print("List after insert:", my_list)

# 5. Pop (ამოიღე ბოლო ელემენტი)
my_list = [1, 2, 3, 4, 5]
my_list.pop()
print("List after pop:", my_list)

# 6. Length (დათვალე ელემენტების რაოდენობა)
my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print("Length of list:", list_length)
