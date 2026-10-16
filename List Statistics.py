numbers = list(map(int,input("Enter numbers separated by spaces: ").split()))

if numbers:
    largest = max(numbers)
    smallest = min(numbers)
    average = sum(numbers) / len(numbers)

    
    print(f"\n--- Total Numbers Entered: {len(numbers)} ---")
    print("\n--- List Statistics ---")

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Average: {average:.2f}")


else:
    print("The list is empty.")