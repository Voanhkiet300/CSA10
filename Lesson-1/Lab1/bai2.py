class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def calPerimeter(self):
        return 2 * (self.height + self.width)
    
    def calArea(self):
        return self.height * self.width
    

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def calPerimeter(self):
        return (self.radius * 3.14) * 2
    
    def calArea(self):
        return self.radius**2 * 3.14
    

shape = input("Shape (rectangle|circle): ")
match shape:
    case "rectangle":
        height = int(input("Height: "))
        width = int(input("Width: "))
        rectangle = Rectangle(height, width)
        print("Perimeter:", rectangle.calPerimeter())
        print("Area:", rectangle.calArea())

    case "circle":
        radius = int(input("Radius: "))
        circle = Circle(radius)
        print("Perimeter:", circle.calPerimeter())
        print("Area:", circle.calArea())
    
    case _:
        print("Invalid!")