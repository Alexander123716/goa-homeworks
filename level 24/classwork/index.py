my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # შედეგი: 5

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # შედეგი: [1, 2, 3, 4]


my_list = [1, 2, 3]
my_list.insert(1, 'a')  # 'a' დაამატეთ ინდექსზე 1
print(my_list)  # შედეგი: [1, 'a', 2, 3]


my_list = [1, 2, 3]
popped_item = my_list.pop(1)  # ამოიღე ელემენტი ინდექსზე 1
print(my_list)  # შედეგი: [1, 3]
print(popped_item)  # შედეგი: 2


my_list = [1, 2, 3, 2]
my_list.remove(2)  # ამოიღე პირველი 2
print(my_list)  # შედეგი: [1, 3, 2]


my_list = [1, 2, 3]

# len()
print("Length of list:", len(my_list))  # შედეგი: 3

# append()
my_list.append(4)
print("List after append:", my_list)  # შედეგი: [1, 2, 3, 4]

# insert()
my_list.insert(1, 'a')
print("List after insert:", my_list)  # შედეგი: [1, 'a', 2, 3, 4]

# pop()
popped_item = my_list.pop(2)
print("List after pop:", my_list)  # შედეგი: [1, 'a', 3, 4]
print("Popped item:", popped_item)  # შედეგი: 2

# remove()
my_list.remove('a')
print("List after remove:", my_list)  # შედეგი: [1, 3, 4]
