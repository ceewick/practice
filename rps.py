# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:01:14 2017

@author: cwickham
"""

'''
Goal

Ask the player if they pick rock paper or scissors
Have the computer chose its move
Compare the choices and decide who wins
Print the results

Subgoals

Let the player play again
Keep a record of the score e.g. (Player: 3 / Computer: 6)
'''

import random

d = {'win':[('r','s'), ('p','r'), ('s','p')],
            'lose':[('r', 'p'), ('s','r'),('p','s')]
            }

userScore = 0
cpuScore = 0

while True:
    choice = str(input('Enter R, P, or S (Type "quit" to quit): '))
    choice = choice.lower()
    l = ['r', 'p', 's']
    if choice == 'quit':
        break
    cpu = random.choice(l)
    match = (choice, cpu)
    if match in d['win']:
        print('Winner! {} vs {}'.format(choice, cpu))
        userScore += 1
    elif match in d['lose']:
        print('Loser! {} vs {}'.format(choice, cpu))
        cpuScore += 1
    elif choice not in l:
        print('Wrong input')
    else:
        print('Tie!! {} vs {}'.format(choice, cpu))
    print('User = {} CPU = {}'.format(userScore, cpuScore))