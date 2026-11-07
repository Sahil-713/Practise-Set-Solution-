def merge_list (list1, list2):
    return list(dict.fromkeys(list1 + list2))

list1 = [10, 20, 30, 40 ,50]
list2 = [40, 50, 60, 70, 80, 90, 100]

result = merge_list(list1, list2)

print("Merge list: ", result)