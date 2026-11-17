# Helper function to check prime number
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Taking input from the user
user_input = input("Enter numbers separated by spaces: ")

# Converting input into a list of integers
numbers = [int(x) for x in user_input.split()]

# Using list comprehension to filter prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime numbers:", prime_numbers)