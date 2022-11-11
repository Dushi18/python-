# program to take operator and two numbers as input and print the correct result
# except : 45*3 = 555, 56 +9 =77 and 56/6 = 4
print("input the operator you want to use")
print("type:\n 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division. ")
scan = input()
print("enter first number")
a = input()
print("enter another number")
b = input()
if int(scan)==1:
    if int(a)==56 and int(b)==9:
        print("the addition of two numbers is 77")
    else:
        print("the addition of two numbers is", int(a)+int(b))
elif int(scan)==2:
    print("the subtraction of two numbers is ",int(a)-int(b))
elif int(scan)==3:
    if int(a)==45 and int(b)==3:
        print("the multiplication of two numbers is 555")
    else:
        print("the multiplication of two numbers is", int(a) * int(b))
elif int(scan)==4:
    if int(a)==56 and int(b)==6:
        print("the division of two numbers is 4")
    else:
        print("the division of two numbers is ", int(a)/int(b))
else:
    print("Invalid input.\nPlease enter operator from 1,2,3 and 4.")