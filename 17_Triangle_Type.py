'''
Problem: Determine Triangle Type

Given the lengths of the sides of a triangle, determine if the triangle is equilateral, isosceles, or scalene.

Parameters:
x (int): Length of the first side of the triangle.
y (int): Length of the second side of the triangle.
z (int): Length of the third side of the triangle.

Returns:
str: Type of the triangle (Equilateral, Isosceles, or Scalene).
'''

def determine_triangle_type(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x != y and y != z and x != z:
        return "Scalene triangle"
    else:
        return "Isosceles triangle"

# Test examples
test_triangles = [(3, 3, 3), (5, 4, 6), (5, 5, 8)]

# Iterate through each set of triangle sides and determine its type
for sides in test_triangles:
    triangle_type = determine_triangle_type(*sides)
    print(f"Triangle with sides {sides}: {triangle_type}")
