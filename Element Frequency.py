def element_frequency (numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency

li = [13, 5, 6, 7, 11, 6, 7, 13, 6, 4, 7,]

print("Element frequency : ",element_frequency(li))