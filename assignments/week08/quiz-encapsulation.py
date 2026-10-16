"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def getArea(self):
        return f"Area of Rectangle: {self.__width * self.__length}"
    
    def getPerimeter(self):
        return f"Perimeter of Rectangle: {2 * (self.__width + self.__length)}\n"
    
    def isSquare(self):
        return self.__width == self.__length
    
myRectangle = Rectangle(5, 10)
print(myRectangle.getArea())
print(myRectangle.getPerimeter())

myRectangle2 = Rectangle(10, 10)
print(myRectangle2.getArea())
print(myRectangle2.isSquare())
