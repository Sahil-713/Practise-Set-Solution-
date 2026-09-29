#Program  to calculate an electricity bill based on slabe rate
Units = float(input("Enter the Electricity Bill: "))

if Units <= 100:
    Bill = Units * 5
elif Units <= 200:
    Bill = (100 * 5) + ((Units - 100) * 7)
elif Units <= 300:
    Bill = (100 * 5) + (100 * 7) + ((Units - 200) * 9)
else:
    Bill = (100 * 5) + (100 * 7) + (100 * 9) + ((Units - 300) * 12)

print("\n--- Electricity Bill ---")
print("Unit Consumed:", Units)
print("Total Bill:", Bill, "Rupess Only-/")

