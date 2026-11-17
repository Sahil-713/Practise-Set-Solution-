# Recursive function to check whether a string is a palindrome
def is_palindrome(s):

    # Base condition: Empty string or single character is a palindrome
    if len(s) <= 1:
        return True

    # If first and last characters are not equal
    if s[0] != s[-1]:
        return False

    # Recursive call: Check the remaining substring
    return is_palindrome(s[1:-1])


# Taking input from the user
string = input("Enter a string: ")


# Convert string into lowercase
string = string.lower()

# Calling the function and displaying the result
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
