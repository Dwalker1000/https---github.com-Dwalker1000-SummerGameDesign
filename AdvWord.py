#Daniel Walker
import os
import random
os.system('cls')

def menu():
    loop = True
    while(loop):
        x = 0
        print("===============================")
        print("|       Guess the word        |")
        print("| 1. Instructions             |")
        print("| 2. Fruit (easy)             |")
        print("| 3. Computer Parts (medium)  |")
        print("| 4. Video Games (hard)       |")
        print("| 5. Exit                     |")
        print("===============================")
        
        while(x < 1 or x > 5):
            try:
                x = int(input("Enter a number(1-5): "))
            except:
                print("Please enter a number")
        
        if x == 1:
            instruct()
        elif x == 2:
            fruit()
        elif x == 3:
            comp()
        elif x == 4:
            vgames()
        elif x == 5:
            loop = False
            break

def instruct():
    os.system('cls')
    print("===================================")
    print("|      Pick a topic from the      |")
    print("|    list and guess the random    |")
    print("|     word based on the topic     |")
    print("|  you will have 5 guesss a word  |")
    print("===================================")
    print()

def fruit():
    os.system('cls')
    fruit = ["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Cherry", "Coconut", "Cucumber", "Durian"]
    randy = random.choice(fruit)

    for i in range(5):
        user = input("Guess a fruit: ")
        if user.lower() == randy.lower():
            print("congrates you guesed the word in", i+1, "guesses")
            break
        elif(i == 4):
            print("you did not get the word correcly")
        else:
            print("Good guess", 4-i, "guesses left")

def comp():
    os.system('cls')
    part = ["CPU", "GPU", "Power supply", "RAM", "Heat sink", "motherboard", "coolant", "water cooled", "SSD", "hard drive"]
    randy = random.choice(part)

    for i in range(5):
        user = input("Guess a Computer Part: ")
        if user.lower() == randy.lower():
            print("congrates you guesed the word in", i+1, "guesses")
            break
        elif(i == 4):
            print("you did not get the word correcly")
        else:
            print("Good guess", 4-i, "guesses left")

def vgames():
    os.system('cls')
    Game = ["Call of duty", "Fortnite", "Minecraft", "Plants vs Zombies", "Bloons Tower Defence", "Clash Royale", "Clash of Clans", "Stumble Guys", "Ratchet and Clank", "Miles Morales"]
    randy = random.choice(Game)

    for i in range(5):
        user = input("Guess a Video Game: ")
        if user.lower() == randy.lower():
            print("congrates you guesed the word in", i+1, "guesses")
            break
        elif(i == 4):
            print("you did not get the word correcly")
        else:
            print("Good guess", 4-i, "guesses left")

menu()