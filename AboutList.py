#Daniel Walker
#Learning about list
#We are also goint to leanr about for loops
import random
import os
os.system('cls')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#              0         1         2        3        4        5        6
#                                          -4       -3       -2        -1
print(thislist[1]) #print from a specific index
print(thislist[-1]) #print from the end
print(thislist[2:5]) #print from two value the first one is included in the set the second is exculuded
print(thislist[:3]) #print up to a value but not including a value
print(thislist[2:]) #prints everything after a value including the original element
print(thislist[-4:-1]) #range of negitive indexes

if "apple" in thislist: #checks for a value in a list
    print("yes the apple is in the list")

for num in range(10): # loops a specific number of times
    print(num, end = " ")
print()

for element in thislist: # element = thislist[times run throught the loop]
    print(element, end = " ")
print()

thislist.append("pinaple") #add a element to the end of a list
print(thislist[0:])

# for num in range(2):
#     thislist.append(input("input a food "))
# print(thislist[0:])

thislist.insert(1, "pinaple") # adding a element to a specific index insert(index, element you want to add)
print(thislist[0:])

for i in range(len(thislist)): # loops for the length of the list
    print(thislist[i], end = " / ")
print()

list_num = [1, 2, 3, 4]
list_num.extend(thislist) #add the elemnts from one list to another
print(list_num)

list_num = [1, 2, 3, 4]
list_num.append(thislist) #add the whole list to the last index
print(list_num)
print(list_num[-1]) # print the last element 
print(list_num[-1][0]) # print a element in in an element if that element is ia list [0, 1, 2, 3, [list2]] [index in list one][index in list 2 if aplicable]

word = random.choice(thislist) #picks a random element in the list
print(word)

guess = input("input a food: \t")
if guess in word:
    print("congrats you guessed the food")