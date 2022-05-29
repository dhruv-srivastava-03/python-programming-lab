from math import pi


def area(radius):
    return (pi*radius*radius)


def perimeter(radius):
    return(2*pi*radius)


radius = int(input("Enter the radius of the circle in cm: "))

print(area(radius))
print(perimeter(radius))
