list1=[]
sum1=0
count=int(input("Enter number of values to insert:\n"))

for _ in range(count):
    value=int(input("Enter value:\n"))
    list1.append(value)

for i in range(count):
    sum1=sum1+list1[i]
print("Sum of all items in list is: ",sum1)
