#Function to reverse a string using recursion:
def reverse_string(s):
    #Base Condition: If the string is empty, return it
    if len(s) == 0:
        return s

    #Recursion Call: Reverse the remaining string
    return reverse_string(s[1:]) + s[0]

#Taking input from the user
string = input("Enter a String: ")

#Calling the function
result = reverse_string(string)

#Displaying the reversed string
print("Reversed String: ", result)