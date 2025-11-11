word=input("enter a word : ")
first=word[0]
nword=first+word[1:].replace(first,'$')
print(nword)
