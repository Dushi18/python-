#program to determine whether triangle is scalene, equialeteral or isosceles.
print("enter three sides of a triangle")
x = input()
y = input()
z = input()
if x==y:
    if y==z:
        print("Its an equilateral triangle.")
    else:
        print("Its an isosceles triangle.")
else:
    if y==z:
        print("Its an isosceles triangle.")
    else:
        print("Its an scalene triangle.")