import os
import random
os.system('cls')

print("===================")
print("|       Title     |")
print("| Instructions1   |")
print("| Instructions2   |")
print("===================")

fruit = ["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Cherry", "Coconut", "Cucumber", "Durian"]
user = input("Guess a fruit: ")
randy = random.choice(fruit)
if user.lower() == randy.lower():
    print("you win")
else:
    print("you louse")