#Generate a list containing only prime number between in 1 and 100 using list comprehension.
Prime_Num = []

for num in range (1,101):
    if all(num % i !=0 for i in range(2,num)):
        Prime_Num.append(num)

print(Prime_Num)