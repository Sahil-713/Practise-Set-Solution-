def ascending_order(numbers):
    n =len(numbers)

    for i in range(n):
        for j in range(0, n - 1):

            if numbers[j] > numbers [j + 1]:
                numbers[j], numbers [j + 1] = numbers [j + 1], numbers [j]

    return numbers

li = [5, 2, 3, 8, 1, 9, 0, 4, 6, 10, 7]

print("Ascending Order: ", ascending_order(li))