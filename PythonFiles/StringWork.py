import os
os.system('cls')

#problem 1.1
str1 = "James"
print(str1[0], end = "")
print(str1[int(len(str1)/2)], end = "")
print(str1[len(str1)-1])

#problem 1.2
str1 = "JhonDipPeta"
print(str1[(int(len(str1)/2) - 1):(int(len(str1)/2) + 2)])

#problem 2
print(str1[int(len(str1)/2) - 1], end = "")
print(str1[int(len(str1)/2)], end = "")
print(str1[int(len(str1)/2) + 1])

#problem 3
s1 = "Ault"
s2 = "Kelly"
s1, s2 = "Ault", "Kelly"
word = s1[:int(len(s1)/2)] + s2 + s1[int(len(s1)/2):]
print(word)

#problem 4
s1, s2 = "America", "Japan"
word = s1[0] + s2[0] + s1[int(len(s1)/2)] + s2[int(len(s1)/2-1)] + s1[-1] + s2[-1]
print(word)

#problem 5
s = "PyNaTive"
cap = {}
x = 0
for i in s:
    if i.islower():
        print(i, end = "")
    else:
        cap[x] = i
        x += 1

for i in range (x):
    print(cap[i], end = "")