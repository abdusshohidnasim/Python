def triangel(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

def area_of_circle(radius):
    pi = 3.14159
    return pi * radius ** 2 