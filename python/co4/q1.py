class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
        
    def display(self):
        print("area:",self.area())
        print("perimeter",self.perimeter())
r1=rectangle(5,10)
r2=rectangle(6,8)
if r1.area()>r2.area():
    print("rectangle 1 has larger area")
else:
    print("rectangle 2 has larger area")

