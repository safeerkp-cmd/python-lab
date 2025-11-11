word=input("enter a word : ")
if len(word)>1:
    nword=word[-1]+word[1:-1]+word[0]
else:
    nword=word
print(nword)    
