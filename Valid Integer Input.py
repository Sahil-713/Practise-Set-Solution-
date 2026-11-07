while True:
    try:
        num = int(input("Enter an integer: "))
        print("Valid integer:", num)
        break

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
