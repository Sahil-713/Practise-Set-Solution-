def finding_number(numbers, n):
    total = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return total - actual_sum

li = [1, 2, 3, 5, 6, 7]
n = 7

print("Missing Number: ", finding_number(li, n))