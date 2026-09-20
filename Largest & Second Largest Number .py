# Finding the Largest & Second Largest amoung three Number

Num_1 = int(input("Enter the Number: "))
Num_2 = int(input("Enter the Number: "))
Num_3 = int(input("Enter the Number: "))

if Num_1 >= Num_2 and Num_1 >= Num_3:
     Largest = Num_1
     if Num_2 >= Num_3:
          Second_largest = Num_2
     else:
          Second_largest = Num_3

elif Num_2 >= Num_1 and Num_2 >= Num_3:
     Largest = Num_2
     if Num_1 >= Num_3:
          Second_largest = Num_1
     else:
          Second_largest = Num_3

else:
     Largest = Num_3
     if Num_1 >= Num_2:
          Second_largest = Num_1
     else:
          Second_largest = Num_2

print("\n--- Result ---")
print("Largest Number: ",Largest)
print("Second Largest Number: ",Second_largest)
     
     
        

