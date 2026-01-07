class rectangle:
    def __init__(self,bredth,length):
        self.__bredth=bredth
        self.__length=length

    def area(self):
        return self.__length*self.__bredth

    def __lt__(self,other):
        return self.area()<other.area()
obj=rectangle(5,3)
obj1=rectangle(3,4)

print(obj<obj1)
            
        
