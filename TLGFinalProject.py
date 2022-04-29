#!/usr/bin/python3

#asciidemo.py
import asciidemo

print(asciidemo.a)                                                                                                                                          
                               

print("Welcome to the Mystical, Magical, and Perfect Magic 8 ball!\n")

print ("\nNote: Don't take this Python program's answers seriously. If you do, you might be worse off in life than you originally thought.\n")


# Import the modules
import sys
import random

ans = True

while ans:
    question = input("\nAsk the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,20)

    if question == "":
        print(asciidemo.z)
        sys.exit()

    elif answers == 1:
        print("It is certain")
        print(asciidemo.c)

    elif answers == 2:
        print("It is decidedly so.")
        print(asciidemo.d)

    elif answers == 3:
        print("Without a doubt.")
        print(asciidemo.e)

    elif answers == 4:
        print("Yes definitely.")
        print(asciidemo.f)

    elif answers == 5:
        print("As I see it, yes.")
        print(asciidemo.g)

    elif answers == 6:
        print("Most likely.")
        print(asciidemo.h)

    elif answers == 7:
        print("Yes.")
        print(asciidemo.i)

    elif answers == 8:
        print("Signs point to yes.")
        print(asciidemo.j)

    elif answers == 9:
        print("Outlook good")
        print(asciidemo.k)

    elif answers == 10:
        print("You may rely on it")
        print(asciidemo.l)

    elif answers == 11:
        print("Ask again later")
        print(asciidemo.m)

    elif answers == 12:
        print("Concentrate and ask again")
        print(asciidemo.m)

    elif answers == 13:
        print("Reply hazy, try again")
        print(asciidemo.m)

    elif answers == 14:
        print("Better not to tell you now.")
        print(asciidemo.n)

    elif answers == 15:
        print("Cannot predict now.")
        print(asciidemo.o)

    elif answers == 16:
        print("My reply is no")
        print(asciidemo.p)

    elif answers == 17:
        print("My sources say no")
        print(asciidemo.q)

    elif answers == 18:
        print("Don't count on it.")
        print(asciidemo.r)

    elif answers == 19:
        print("Outlook not so good.")
        print(asciidemo.s)

    elif answers == 20:
        print("Very doubtful.")
        print(asciidemo.t)
