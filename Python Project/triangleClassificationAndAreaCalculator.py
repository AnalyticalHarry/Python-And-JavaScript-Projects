#import math
import math
#import random modules
import random

#creating class triangles
class Triangle:
    #initialising the class with three sides
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    #method for checking if given side are valid
    def is_valid(self):
        #side 1 + side 2 > side 3
        #side 2 + side 3 > side 1
        #side 3 + side 1 > side 2
        return (self.side1 + self.side2 > self.side3) and (self.side2 + self.side3 > self.side1) and (self.side3 + self.side1 > self.side2)
        
    #method for checking the type of the triangle (Equilateral, Isosceles, or Scalene)
    def type(self):
        if not self.is_valid():
            return "Invalid triangle"
            
        if self.side1 == self.side2 == self.side3:
            return "Equilateral triangle"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side3 == self.side1:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"
    #type of angles in the triangle (Acute, Right, or Obtuse)
    def angle_type(self):
        if not self.is_valid():
            return "Invalid triangle"
        #sorting sides
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        #determining the side of triangles
        a, b, c = sides

        if a**2 + b**2 > c**2:
            return "Acute triangle"
        elif a**2 + b**2 == c**2:
            return "Right triangle"
        else:
            return "Obtuse triangle"
    #method to calulate are of traingles
    def area(self):
        if not self.is_valid():
            return "Invalid triangle"
        #formula
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return round(area,2)
        
    #method to print output
    def __str__(self):
        return f"Triangle with sides {round(self.side1, 2)}, {round(self.side2, 2)}, {round(self.side3, 2)}"

#Equilateral triangle with Acute angles
equilateral_acute = Triangle(5, 5, 5)
print(f"CEquilateral triangle with Acute angles:")
print(equilateral_acute)
print(f"Type: {equilateral_acute.type()}")
print(f"Angle Type: {equilateral_acute.angle_type()}")
print(f"Area: {equilateral_acute.area()}\n")

#Isosceles triangle with Right angles
isosceles_right = Triangle(4, 4, math.sqrt(32))
print(f"CIsosceles triangle with Right angles:")
print(isosceles_right)
print(f"Type: {isosceles_right.type()}")
print(f"Angle Type: {isosceles_right.angle_type()}")
print(f"Area: {isosceles_right.area()}\n")

#Scalene triangle with Obtuse angles
scalene_obtuse = Triangle(7, 9, math.sqrt(155))
print(f"Scalene triangle with Obtuse angles:")
print(scalene_obtuse)
print(f"Type: {scalene_obtuse.type()}")
print(f"Angle Type: {scalene_obtuse.angle_type()}")
print(f"Area: {scalene_obtuse.area()}\n")
