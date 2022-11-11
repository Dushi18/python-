# printing name of user and reversing it
print("enter your first name")
first = input()
print("enter your last name")
last = input()
print("your full name is", first, last)
(first, last) = (last, first)
print("your reversed name is", first, last)
