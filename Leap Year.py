# Calculate whether the given year is a leap year or not.

Year = int(input("Enter the Year:"))

# Use nested if statements to check whether the given year is a leap year.
if Year % 4 == 0:                        # The year must be divisible by 4.
    if Year % 100 == 0:                  # If divisible by 100, it must also be divisible by 400.
        if Year % 400 == 0:  
            print(Year,"is a Leap year")
        else:
            print(Year,"is not a Leap year")
    else:
        print(Year,"is a Leap year")
else:                                    # If not divisible by 4, it is not a leap year.
    print(Year,"is not a Leap year")
