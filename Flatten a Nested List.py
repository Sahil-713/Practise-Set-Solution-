
# Recursive function to flatten a nested list
def flatten_list(nested_list):

    # Create an empty list to store flattened elements
    result = []

    # Iterate through each element
    for item in nested_list:

        # Check if the element is another list
        if isinstance(item, list):

            # Recursive call to flatten the inner list
            result.extend(flatten_list(item))

        else:
            # Add normal elements to the result
            result.append(item)

    # Return the flattened list
    return result


# Original nested list
nested_list = [1, [2, 3], [4, [5, 6]], 7]

# Call the recursive function
flat_list = flatten_list(nested_list)

# Display the result
print("Original List:", nested_list)
print("Flattened List:", flat_list)
