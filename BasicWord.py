#Daniel Walker
import os
import random
os.system('cls')

print("===============================")
print("|       Guess the Fruit       |")
print("|   guess the correct fruit   |")
print("|      from a list to win     |")
print("===============================")

fruit = ["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Cherry", "Coconut", "Cucumber", "Durian"]
user = input("Guess a fruit: ")
randy = random.choice(fruit)
if user.lower() == randy.lower():
    print("you win")
else:
    print("you louse")