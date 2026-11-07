my_list = ["Apple", " ", "Banana", "Pineapple", "" ]

new_list = [word for word in my_list if word.strip()]
print(new_list)