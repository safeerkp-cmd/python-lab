text=input("enter a line of text: ")
words=text.split()
wcount={}

for i in words:
    if i in wcount:
        wcount[i]+=1
    else:
        wcount[i]=1
print(wcount)        
