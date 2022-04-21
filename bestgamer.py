#!/usr/bin/env python3

print('Welcome to the best Gaming Platform Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite gaming platform? PC or Console?')
    if answer=='PC':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Should you play on any other platforms besides PC? (yes/no) ')
    if answer.lower()=='no':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of the best gaming platform?')
    if answer=='PC':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 4: Do you have to pay a service to play with most  games online with PC? (yes/no)')
    if answer=='no':
        score+= 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 5: Is the nickname for PC users PC Peasant Race? (yes/no)')
    if answer=='no':
        score+= 1
        print('correct. It is actually PC Master Race')
    else:
        print('Wrong Answer. It is actually PC Master Race')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE! PC MASTER RACE!!! ')
