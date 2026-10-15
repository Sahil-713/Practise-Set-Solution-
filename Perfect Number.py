num = int(input("Enter a Number: "))
sum_factor = 0

for i in range (1, num):
    if num % i == 0:
        sum_factor += i

if sum_factor == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")