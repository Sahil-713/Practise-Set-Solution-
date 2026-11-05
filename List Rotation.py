li = [1, 2, 3, 4, 5]
k = 2
k = k % len (li)
r = li [k:] + li [:k]

print("List Rotation:",r)