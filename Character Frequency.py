text = input("Enter a string : ")#.lower() if uppercase and lowercase letters should be counted as the same character.
frequency = {}     

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"{char} : {count}")
