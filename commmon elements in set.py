# checking common elements in set and print them
set1 = {1,3,5,7,9}
set2 = {4,6,8,10,11}
# print('ram' in set1)
if set1.intersection(set2):
    print("yes there are some common elements ")
    print(set1.intersection(set2))
else:
    print("no common elements")
