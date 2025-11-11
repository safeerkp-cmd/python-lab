n=int(input("Enter number of terms to print its fibonacci sequence: \n"))
count=0
a=0
b=1
while count<n:
    print(a," ")
    next=a+b
    a=b
    b=next
    count+=1
