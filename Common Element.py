def common_elements(list1, list2):
    common = []

    for num in list1:
        if num in list2 and num not in common:
            common.append(num)

    return common

list1 = [5, 10, 15, 20, 25, 30]
list2 = [25, 30, 35, 40, 45, 50]

print("Common Element:", common_elements(list1, list2))