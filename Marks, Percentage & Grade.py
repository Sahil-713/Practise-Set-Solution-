# Write a Programto input in five subject and calculate the total, percentage, and grade.
Math = float(input("Enter the marks of Math:  "))
Science = float(input("Enter the marks of Science: "))
Hindi = float(input("Enter the marks of Hindi: "))
English = float(input("Enter the marks of English: "))
Social_Studies = float(input("Enter the marks of Social_Studies: "))

#Calculating the total & Percentage.
Total = Math + Science + Hindi + English + Social_Studies
Percentage = Total / 5

# Grade:
if Percentage >=90:
    Grade = "A+"
elif Percentage >=80:
    Grade = "A"
elif Percentage >=70:
    Grade = "B"
elif Percentage >=60:
    Grade = "C"
elif Percentage >=50:
    Grade = "D"
else:
    Grade = "F"

print("\n--- Result ---")
print("Total Marks :",Total)
print("Percentage: ",Percentage)
print("Grade: ",Grade)


