class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        result = self.lenght * self.width
        return result

    def perimeter(self):
        result = 2 * self.lenght + 2 * self.width
        return result


Rectangle = Rectangle(4, 3)
print(Rectangle.area())
print(Rectangle.perimeter())
