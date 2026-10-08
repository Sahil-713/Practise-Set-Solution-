#Program to check wheather a number is an Armstrong Number.

Number = int(input("Enter the Number : "))

Original_Number = Number
Number_of_Digit = len(str(Number))
SUM = 0

while Number > 0:
    Digit = Number % 10

    SUM = SUM + Digit ** Number_of_Digit

    Number = Number // 10

if SUM == Original_Number :
    print(f"{Original_Number} is an Armstrong Number")
else:
    print(f"{Original_Number} is not an Armstrong Number")