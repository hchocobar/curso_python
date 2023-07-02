# Python One-Liners

# It's a comprehensive guide to practicing Python one-liners, including List comprehension [ ], Dict comprehension {
# }, and much more.

# Assigning multiple values to variables
name, quantity, price = 'Book', 3, 4.99
print(name, quantity, price)  # Output: Book 3 4.99

# Conditional [ ] list comprehension
one = ['a', 1, 'b', 'b', 4, '1']
two = ['h', 'l', 1, 'a', 'j', '1'] 
common = [x for x in one if x in two]
print(common)  # Output: ['a', 1, '1']

# List [ ] comprehension
lib = [4, 8, 2, 4, 0, 3]
double_nums = [num * 2 for num in lib]
print(double_nums)  # Output: [8, 16, 4, 8, 0, 6]

# Swapping two variables
a = 1
b = 2
a, b = b, a
print(a, b)  # Output: 2 1

# Conditional comprehension, ternary operator
one = [1, 2, 3, 4, 5, 6, 7]
new = [x if x % 2 == 0 else x * 2 for x in one]
print(new)  # Output: [2, 2, 6, 4, 10, 6, 14]

# Reverse []
one = ['a', 'b', 'c', 'd', 'e']
two = one[::-1]
print(two)  # Output: ['e', 'd', 'c', 'b', ‘a']
# or
three = ['a', 'b', 'c', 'd', 'e'][::-1]
print(three)  # Output: ['e', 'd', 'c', 'b', 'a']

# Check for False
a = [True, True, True]
b = [True, True, False]
print(all(a))  # Output: True
print(all(b))  # Output: False

# Printing elements of a collection
a = [1, 2, 'three', 4, 5]
print(a)  # Output: [1, 2, ‘three', 4, 5]
print(*a)  # Output: 1 2 three 4 5

# Converting string with numbers to integer []
a = '1 2 3 4 5'
b = list(map(int, a.split()))
print(b)  # Output: [1, 2, 3, 4, 5]

# Find the Most Frequent Element []
a = [4, 1, 2, 2, 3, 3, 3]
most_frequent = max(set(a), key=a.count)
print(most_frequent)  # Output: 3

# Unique values only []
values = ['h', 1, 'b', 'b', 4, '1', 'a', 4]
option_1 = list({x for x in values})
print(option_1)  # Output: [1, 'h', 4, 'a', 'b', ‘1’]
# or
option_2 = list(set(values))
print(option_2)  # Output: [1, 'h', 4, 'a', 'b', ‘1’]
# or
option_3 = [x for x in set(values)]
print(option_3)  # Output: [1, 'h', 4, 'a', 'b', ‘1']
# or
option_4 = []
[option_4.append(x) for x in values if x not in option_4]
print(option_4)  # Output: ['h', 1, 'b', 4, '1', 'a']

# Traverse []
one = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
result_slice = one[2:6:2]
print(result_slice)  # Output: ['c', ‘e']
# or
result_comprehension = [x for x in one[2:6:2]]
print(result_comprehension)  # Output: ['c', ‘e']

# Merge two lists into {:}
one = [1, 2, 3, 4, 5]
two = ['a', 'b', 'c', 'd', 'e']
hm_1 = dict([(one[i], two[i]) for i in range(len(one))])
print(hm_1)  # Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# or
hm_2 = {one[i]: two[i] for i in range(len(one))}
print(hm_2)  # Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# Moderate {:}
old_stock = {'water': 1.42, 'cheese': 2.5, 'milk': 2.0}
price = 0.76
correction = {item: value*price for (item, value) in old_stock.items()}
print(correction)  # Output: {'water': 1.0792, 'cheese': 1.9, 'milk': 1.52}
