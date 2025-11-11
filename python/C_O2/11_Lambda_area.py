square_area   = lambda side: side * side
rectangle_area = lambda length, width: length * width
triangle_area  = lambda base, height: 0.5 * base * height

print("Area of square (side=5):", square_area(5))
print("Area of rectangle (length=4, width=6):", rectangle_area(4, 6))
print("Area of triangle (base=10, height=8):", triangle_area(10, 8))
