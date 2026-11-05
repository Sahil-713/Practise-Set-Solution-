li = [1, 1, 2, 3, 4, 4, 5, 6,]
unique_li = []

for num in li:
    if num not in unique_li:
        unique_li.append(num)
print(unique_li)
