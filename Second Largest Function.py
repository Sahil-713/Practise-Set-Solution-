def second_largest(numbers):
    unique_list = sorted(set(numbers))

    if len(unique_list) < 2:
        return None

    return unique_list[-2]


my_list = [10, 20, 5, 15, 30, 40, 35, 45]

print("Second Largest", second_largest(my_list))
