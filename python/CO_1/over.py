num=[int(x)for x in input("enter integer: ").split()]
res=[]
for n in num:
    if n>100:
        res.append("over")
    else:
        res.append(n)
print(res)
