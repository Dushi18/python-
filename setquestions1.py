#write a python program to print out a set containing all the colors from color_list1 which are not prsesnt in color_list2
color_list1 = {'blue', 'red', 'orange', 'green', 'black'}

color_list2 = {'orange','pink', 'purple'}
# print(type(color_list1))
a = color_list1.intersection(color_list2)
b = color_list1-a
print(b)
# print("set of colours of list 1 which are not in list2")
# print(color_list1-color_list1.intersection(color_list2))