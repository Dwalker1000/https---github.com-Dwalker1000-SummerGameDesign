import os, datetime
os.system('cls')
name = "Daniel"
score = 100
date = datetime.datetime.now()
print(date.strftime("%m/%d/%y"))
print(date.strftime("%Y  %m  %d"))
scoreLn = str(score) + "\t" + name + "\t" + date.strftime("%m/%d/%y") + "\n"
print(scoreLn)

#file writing
myFile = open("scre.txt", 'w') #writing to file
myFile.write(scoreLn)
myFile.close()

#File appending
myFile = open("scre.txt", "a")
myFile.write(scoreLn)
myFile.close()

#File Reading
myFile = open("scre.txt", "r")
for line in myFile:
    print(line)
myFile.close()