# Function to calculate factorial using recursion
def factorial(num):

    # Base condition: factorial of 0 and 1 is 1
    if num == 0 or num == 1:
        return 1

    # Recursive call: multiply number by factorial of previous number
    else:
        return num * factorial(num - 1)


# Take input from the user
number = int(input("Enter a number: "))

# Check for negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Call the factorial function and display the result
    print("Factorial of", number, "is:", factorial(number))
