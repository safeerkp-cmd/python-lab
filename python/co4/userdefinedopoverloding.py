class Rectangle:
    def __init__(self,length,bredth):
        self.__length=length
        self.__bredth=bredth
    def area(self):
        return self.__length*self.__bredth
    def __lt__(self,other):
        return self.area()<other.area()
    
l1=int(input("enter length of first rectangle:"))
l2=int(input("enter bredth of first rectangle:"))
l3=int(input("enter length sec rect:"))
l4=int(input("enter breadth sec rect:"))
obj=Rectangle(l1,l2)
obj1=Rectangle(l3,l4)

if(obj<obj1):
    print("first recangle1 has small area than rect2 ")
else:
    print("first recangle2 has small area than rect1 ")
    
