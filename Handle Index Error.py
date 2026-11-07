my_list = [10, 20, 30, 40, 50] # 1 to 4 Index

try:
    index = int(input("Enter the Index: "))
    print("Element",my_list[index])

except IndexError:
    print("Error: Index is out of range.")

except ValueError:
    print("Error: Please enter a valid integer")
