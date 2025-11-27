class Rectangle:
    def __init__(self, length, width):
        self.__length = length     # private attribute
        self.__width = width       # private attribute

    def area(self):
        return self.__length * self.__width

    # Overloading < operator to return sum of areas
    def __lt__(self, other):
        return self.area() + other.area()


# Example usage
r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)

result = r1 < r2   # uses overloaded < operator
print("Sum of areas:", result)
