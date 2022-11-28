

#!Lists
#List items are ordered, mutable, and allow duplicate values.

list1 = [1,2,3,4,"Zoran"]

print(list1) # [1, 2, 3, 4, 'Zoran']

#! for loop
#best to use range
for x in range(0,len(list1)):
    list1[x] = 5
    print(list1[x])

print(list1)



