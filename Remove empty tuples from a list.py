#Method 1: Using List Comprehension
my_list = [(1, 2), (), (3, 4), (), (5,)]
filtered_list = [tup for tup in my_list if tup]
print("Original list:", my_list)
print("List after removing empty tuples:", filtered_list)

#Method 2: Using filter() function
my_list = [(1, 2), (), (3, 4), (), (5,)]
filtered_list = list(filter(lambda tup: tup, my_list))
print("Original list:", my_list)
print("List after removing empty tuples:", filtered_list)