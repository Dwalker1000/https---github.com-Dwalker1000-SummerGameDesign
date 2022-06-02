# Dainel Walker
# We are going learning strings and the diffrent methods

import os
os.system('cls')

print('Hi')
message = "you are awesome" #a string is an array of characters
#       0 1 2 3 4 5 6 7 ... arrays begin at zero
#       y o u   a r e   ...

print(message)
print(message[5])

wordLength = len(message) # used to calculoate the length of a string
print(wordLength)
print(message[wordLength-1]) # length -1 to get the last charcater in a word

if message.isdigit(): #when usiong methos add a dot on the end
    sum = message + 3   #if the statement is true
    print(sum)
else:                   # if the statement is false
    print(message + " I say so") # concatination

print(message.upper())
print(message)

if message.isupper():
    print(message)
else:
    message = message.upper()
    print(message)

middle = int(wordLength/2)
print(middle)
print(message[middle])

print(message[0:7])
print(message[7:10])

print(help(message.index)) # input the method you want to get info on without the ()