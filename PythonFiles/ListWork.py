#Maria Suarez
#We will learn lists, and list funcs & meth, add elements,delete,
#for  loops
#random class
from mimetypes import guess_all_extensions
import os
import random
os.system('cls')

#A list is an array is indexed, is changeable, is sizeable
#name and use []
myList=[1,2,3,4,5]
#       0 1 2 3 4
#        -3 -2 -1

print(myList)
print(myList[1])# will prinnt elem in position 1
print(myList[1:3]) # print elements 1,2
print(myList[-1])
print(myList[-3:-1]) #print the third and 4th fr left
print(myList[-3:]) #print the last 3
myFruits= ["apple","banana", "kiwi", "papaya","pear"]
print(myFruits[:3])
lengthList=len(myFruits)#Number of elemsnts is always one less than your last index

# print(lengthList)
# print(myFruits[lengthList-1])
# print(myFruits[0])
# print(myFruits[1])
# print(myFruits[2])
#For loop repeats specific number of times

for elem in myFruits: #control the loop   elem is a local var
    print(elem)

for elem in range(lengthList):
    print (elem, end=" = ")
    print(myFruits[elem])

if "apple" in myFruits:
    print("Yes apple is in the list")

myFruits.append("pinaple") # append only add elemnts to the end of teh list
print(myFruits[0:])

myFruits.insert(2, "orange") # insert(index where you want the elment to go, elemnt)
print(myFruits[0:])

print(myList)
myList.extend(myFruits)
print(myList)

myList=[1,2,3,4,5]
print(myList)
myList.append(myFruits)
print(myList)
print(myList[5])
print(myList[5][1])

# myFruits[1] = "hi"
print(myFruits)

for i in range(10):
    element = random.choice(myFruits)
    print(element,  end = "  ")

element = random.choice(myFruits)
print(element)

guess = input("insert a fruit")
if guess.lower() == element.lower():
    print("you guessed correctly")
