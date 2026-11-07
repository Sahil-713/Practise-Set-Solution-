# Menu-driven calculator with exception handling

while True:
    # Display calculator menu
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        # Take the user's choice
        choice = int(input("Enter your choice (1-5): "))

        # Exit the calculator
        if choice == 5:
            print("Calculator closed.")
            break

        # Check whether the selected option is valid
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select 1 to 5.")
            continue

        # Take two numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform calculation based on user's choice
        if choice == 1:
            result = num1 + num2

        elif choice == 2:
            result = num1 - num2

        elif choice == 3:
            result = num1 * num2

        elif choice == 4:
            result = num1 / num2

        # Display the calculation result
        print("Result:", result)

    # Handle invalid input such as letters or symbols
    except ValueError:
        print("Error: Please enter valid numeric input.")

    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
