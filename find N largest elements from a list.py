def find_n_largest_elements(my_list, n):
    if len(my_list) < n:
        return None  
    else:
        sorted_list = sorted(set(my_list), reverse=True)
        return sorted_list[:n]


num_list = [int(x) for x in input("Enter elements of the list separated by spaces: ").split()]


n = int(input("Enter the value of N: "))


result = find_n_largest_elements(num_list, n)


if result is not None:
    print(f"The {n} largest elements in the list are: {result}")
else:
    print("The list has fewer than N elements.")
