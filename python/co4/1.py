class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    # Compare rectangles by area
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()

    def __repr__(self):
        return f"Rectangle({self.length}, {self.breadth})"


# Example usage:
r1 = Rectangle(5, 4)
r2 = Rectangle(6, 3)

print("Area of r1:", r1.area())
print("Perimeter of r1:", r1.perimeter())

print("Area of r2:", r2.area())
print("Perimeter of r2:", r2.perimeter())

# Comparing rectangles
if r1 < r2:
    print("r1 has smaller area")
elif r1 == r2:
    print("Both rectangles have the same area")
else:
    print("r1 has larger area")
