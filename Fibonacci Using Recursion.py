# Function to calculate Fibonacci number using recursion
def fibonacci(num):

    # Base conditions
    if num == 0:
        return 0

    elif num == 1:
        return 1

    # Recursive call: sum of the previous two Fibonacci numbers
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# Take input from the user
n = int(input("Enter the number of terms: "))

# Check for valid input
if n <= 0:
    print("Please enter a positive integer.")

else:
    print("Fibonacci Series:")

    # Print Fibonacci series
    for i in range(n):
        print(fibonacci(i), end=" ")
