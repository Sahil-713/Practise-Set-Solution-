text = input("Enter a string : ")#.lower() if uppercase and lowercase letters should be counted as the same character.
frequencey = {}     

for char in text:
    if char in frequencey:
        frequencey[char] += 1
    else:
        frequencey[char] = 1

for char, count in frequencey.items():
    print(f"{char} : {count}")
