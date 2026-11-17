
import statistics

# Create an empty list to store numbers
numbers = []

# Keep accepting input until the user enters 'stop'
while True:
    user_input = input("Enter a number (or 'stop' to finish): ")

    # Stop taking input
    if user_input.lower() == "stop":
        break

    try:
        # Convert input into a number
        num = float(user_input)

        # Add number to the list
        numbers.append(num)

    except ValueError:
        # Handle invalid input
        print("Invalid input! Please enter a valid number.")

# Check whether the list contains numbers
if len(numbers) > 0:

    # Calculate minimum, maximum, average and median
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    median = statistics.median(numbers)

    # Display results
    print("\nResults:")
    print("Numbers:", numbers)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", average)
    print("Median:", median)

else:
    print("No numbers were entered.")
