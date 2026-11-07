def longest_word(sentence):
    words = sentence.split()
    return max(words, key = len).capitalize()

text = input("Enter a Sentence : ")
print("Longest Word: ", longest_word(text))