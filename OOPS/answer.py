class Shape:
    def area(self):
        print("Area not defined")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = int(input("Enter the radius of circle: "))
    def area(self):
        print(3.14*self.radius**2)  
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = int(input("Enter the length of rectangle: "))
        self.breadth = int(input("Enter the breadth of rectangle: "))
    def area(self):
        print(self.length*self.breadth)
class Square(Shape):
    def __init__(self, side):
        self.side = int(input("Enter the side of square: "))
    def area(self):
        print(self.side*self.side)
circle = Circle(5)
rectangle = Rectangle(4, 6) 
square = Square(4)
print(circle.area())
print(rectangle.area())
print(square.area())