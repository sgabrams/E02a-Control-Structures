#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')# gives grreting to the player
colors = ['red','orange','yellow','green','blue','violet','purple']# provides all possible answers
play_again = ''# gives player option to play again
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):# player not electing to play again by typing no or n
    match_color = random.choice(colors)# out of the given colors the right answer is random
    count = 0 #number of tries is 0 zero
    color = ''# players guessn which color is correct
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()# makes sure that answers are not incorrect if typed in with or  without cpatiatls and spaces
        count += 1# keeps tracks of the player's number of guessing
        if (color == match_color):# describes the instance in which the player is correct
            print('Correct!')# giving the result if the player is correct
        else:# describing if the player guessing incorrectly
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))# giving the result ifn the player is wrong
    
    print('\nYou guessed it in {} tries!'.format(count))# when the game is concluded it gives the amount of guesses that were played

    if (count < best_count):# compares the amount of guesses to other games played 
        print('This was your best guess so far!')# lets the player no that they got it less tries than before
        best_count = count# allows the program to remember that in this instance that its the best try

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()# gives player the option to play again

print('Thanks for playing!')# last statement before the game ends
