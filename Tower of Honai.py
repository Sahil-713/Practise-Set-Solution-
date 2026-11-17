
# Function to solve Tower of Hanoi using recursion
def tower_of_hanoi(n, source, auxiliary, destination):

    # Base condition: If only one disk is left
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move the largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Taking input from the user
n = int(input("Enter the number of disks: "))

# Calling the recursive function
tower_of_hanoi(n, 'A', 'B', 'C')
