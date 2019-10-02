#!/usr/bin/python
print "Welcome to Scott's Die simulator!\n"

import random

question = raw_input('Would you like to roll the die? Yes or No?')

while (question.lower()) != 'no':
        if (question.lower()) == 'yes':
            die1 = random.randint(1, 6)
            print(die1)

        else: 
            print('Invalid response. Please type yes or no.')        

        question = raw_input('Would you like to roll the die again? Yes or no??') 

print('Good-bye!')
