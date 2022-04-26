#!/usr/bin/python3

print("Welcome to the Mystical, Magical, and and Perfect Magic 8 ball!")



print ("Note: Don't take this Python program's answers seriously. If you do, you might be worse off in life than you originally thought.")

# Import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("Outlook good")

    elif answers == 3:
        print("You may rely on it")

    elif answers == 4:
        print("Ask again later")

    elif answers == 5:
        print("Concentrate and ask again")

    elif answers == 6:
        print("Reply hazy, try again")

    elif answers == 7:
        print("My reply is no")

    elif answers == 8:
        print("My sources say no")
