#Define a class Rectangle with attributes length and width. 
#Implement methods to calculate the area and perimeter of the
#rectangle. Create an instance of the class and print the area and perimeter

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return  self.length * self.breadth
    def perimeter(self):
        return  2 * (self.length+self.breadth)


my_rectangle = Rectangle(10, 5)
print(f"Area: {my_rectangle.area()}")
print(f"perimeter: {my_rectangle.perimeter()}")
