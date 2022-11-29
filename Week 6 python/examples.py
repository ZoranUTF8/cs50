

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered ** and changeable. No duplicate members.
'''
'''
#!Lists
#! List items are ordered, mutable, and allow duplicate values.

list1 = [1, 2, 3, 4, "Zoran"]
tupple1 = (1, 2, 3, 4, "Zoran")
set1 = {"zoran", "moeko", "zoran"}
dic1 = {"name": "Zoran", "lname": "Moeko", "pname": "Zoran"}
print(list1)  # [1, 2, 3, 4, 'Zoran']

#!Tuple
#!A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

#!Sets
#!A set is a collection which is unordered, unchangeable, and unindexed.
myset = {"apple", "banana", "cherry"}

#!Dictionaries
#! Dictionaries are used to store data values in key:value pairs.
#!A dictionary is a collection which is ordered, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])

'''


'''
#! for loop
# best to use range
for x in range(0, len(list1)):
    list1[x] = 5
    print(list1[x])

print(list1)

xt = int(5)
print(xt)
'''


print('x', "x")
