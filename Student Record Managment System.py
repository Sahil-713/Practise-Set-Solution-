import csv
import os

# File to store student records
FILE_NAME = "students.csv"


# Function to load student records from the file
def load_students():

    students = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:
        print("No existing records found. Starting a new system.")

    except OSError as e:
        print("Error reading file:", e)

    return students


# Function to save student records into the file
def save_students(students):

    try:
        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = ["id", "name", "age", "marks"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("Records saved successfully.")

    except OSError as e:
        print("Error saving records:", e)


# Function to add a new student
def add_student(students):

    student_id = input("Enter Student ID: ").strip()

    # Check for duplicate student ID
    if any(s["id"] == student_id for s in students):
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter Student Age: "))
        marks = float(input("Enter Student Marks: "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks!")
            return

    except ValueError:
        print("Please enter valid numeric values!")
        return

    # Create a student dictionary
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    save_students(students)

    print("Student added successfully!")


# Function to display all student records
def display_students(students):

    if not students:
        print("No student records available.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Marks: {student['marks']}"
        )


# Function to search for a student
def search_student(students):

    student_id = input("Enter Student ID to search: ").strip()

    # List comprehension to find matching student
    result = [s for s in students if s["id"] == student_id]

    if result:
        print("\nStudent Found:")
        print(result[0])
    else:
        print("Student not found!")


# Function to update student records
def update_student(students):

    student_id = input("Enter Student ID to update: ").strip()

    # Find student using list comprehension
    result = [s for s in students if s["id"] == student_id]

    if not result:
        print("Student not found!")
        return

    student = result[0]

    print("Leave input blank to keep the existing value.")

    name = input("Enter new name: ").strip()

    if name:
        student["name"] = name

    try:
        age = input("Enter new age: ").strip()

        if age:
            age = int(age)

            if age <= 0:
                print("Age must be positive!")
                return

            student["age"] = age

        marks = input("Enter new marks: ").strip()

        if marks:
            marks = float(marks)

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100!")
                return

            student["marks"] = marks

    except ValueError:
        print("Invalid input! Update cancelled.")
        return

    save_students(students)

    print("Student record updated successfully!")


# Function to delete a student record
def delete_student(students):

    student_id = input("Enter Student ID to delete: ").strip()

    # Find student using list comprehension
    result = [s for s in students if s["id"] == student_id]

    if result:
        students.remove(result[0])

        save_students(students)

        print("Student record deleted successfully!")

    else:
        print("Student not found!")


# Main function
def main():

    # Load existing records
    students = load_students()

    while True:

        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            save_students(students)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


# Program execution
if __name__ == "__main__":
    main()
