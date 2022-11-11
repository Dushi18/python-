# lets test your age for driving
print("enter your age")
age = int(input())
if age<100:
    if age > 18:
         print("You can drive")
    elif age == 18:
          print("you can wait for sometime to drive")
    else:
          print("you cannot drive")
else:
    print("please enter a valid age")