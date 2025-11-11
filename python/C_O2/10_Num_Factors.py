num=int(input("Enter a number to print its factors"))
factor=1
print("Factors of", num,"are:\n")
while factor<num:
    if num%factor==0:
        print(factor)
    factor+=1
