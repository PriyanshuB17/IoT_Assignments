# 1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

len =  float(input("Enter the length of rectangle: "))
br = float(input("Enter the breath of rectangle: "))

def area():
    ar = len*br
    return ar

def peri():
    pr = 2*(len+br)
    return pr

print(f"Area of rectangle = {area()}")
print(f"Perimeter of rectangle = {peri()}")

