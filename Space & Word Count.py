text = input("Enter a string : ")

no_spaces = text.replace(" ","")
word_count = len(text.split()) 

print("String without spaces :", no_spaces)
print("Number of words :", word_count)