def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num_1 = int(input("Enter a Number : "))
num_2 = int(input("Enter a Number : "))

print("GCD Number :", calculate_gcd(num_1, num_2))
