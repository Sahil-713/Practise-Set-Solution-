# Checking Palindrome Using Slicing Method

n = input("Enter a word: ").lower().casefold()
# use lower if wrods enter in Caps & Casfold if case-insensitive.

reverse = n [::-1] 

if n == reverse:
    print (f"{n} is a Palindrome")
else:
    print (f"{n} is not a Palindrome")
