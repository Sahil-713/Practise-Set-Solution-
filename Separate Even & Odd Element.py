li = [10, 15 ,20, 25, 30, 35, 40, 45, 50, 55 ]
even_li = []
odd_li = []

for num in li:
    if num % 2 == 0:
        even_li.append(num)
    else:
        odd_li.append(num)

print("Even Numbers:", even_li)
print("Odd Number:", odd_li)