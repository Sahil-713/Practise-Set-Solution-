String = input("Enter a String : ")

Vowels = 0
Consonants = 0
Digits = 0
Special_Characters = 0

for Character in String:

    if Character.lower() in "aeiou":
        Vowels += 1

    elif Character.isalpha():
        Consonants += 1

    elif Character.isdigit():
        Digits += 1

    else:
        Special_Characters += 1

print("Vowels:", Vowels)
print("Consonants:", Consonants)
print("Digits:", Digits)
print("Special Characters:", Special_Characters)