words = input("Enter words separated by spaces: ").split()
max_length=0
for w in words:
    if len(w)>max_length:
        max_length=len(w)
print("Length of the longest word:", max_length)
