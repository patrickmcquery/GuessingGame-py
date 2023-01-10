#This is a guessing game for 1 player
#The range of numbers always starts at 1 and can be changed with the "max" variable
#Players can play multiple games per session and when exiting, will be shown stats

from random import randint
#intro prints the introduction text with the max variable so it is always correct
def intro(max):
    print('This program allows you to play a guessing game.')
    print('I will think of a number between 1 and')
    print(max, ' and will allow you to guess until')
    print('you get it. For each guess, I will tell you')
    print('whether the right answer is higher or lower')
    print('than your guess.\n')

#play contains the main game loops
#it returns the number of guesses for one round of play to be used
#in the results to calculate the stats
def play(max):
    answer = randint(1, max)
    pnumGuesses = 1
    guessing = True
    while(guessing):
        guess = 0
        typing = True
        while(typing):
            guess = input('Your guess? ')
            guess = int(guess)
            if(guess == answer):
                typing = False
            elif(guess < answer):
                print('It\'s higher')
                pnumGuesses += 1
            elif(guess > answer):
                print('It\'s lower')
                pnumGuesses += 1
            
        if(pnumGuesses == 1):
            print('You got it right in 1 guess')
        else:
            print('You got it right in ', pnumGuesses, ' guesses')
        return pnumGuesses

#results calculates the average guesses per game and prints all of the stats
def results(totGuesses, totGames, bestGuess):
    avg = totGuesses / totGames
    print('Overall results: ')
    print('    total games = ', totGames)
    print('    total guesses = ', totGuesses)
    print('    guess/game = ', avg)
    print('    best game = ', bestGuess)

#playAgain checks if the player would like to play another round
#it returns a boolean to determined by the user input
def playAgain():
    while(True):
        response = input('Do you want to play again? ').lower()[0]
        if(response == "y"):
            return True
        elif(response == "n"):
            return False
        else:
            print('Please enter a valid response.')

#initializing neccesary variables
max = 100
totalGuesses = 0
totalGames = 0
bestGuess = 0
playing = True

intro(max)

#Main game loop that repeats games until the player says no
#before exiting, calls the results method to print the stats
while(playing):
    numGuesses = play(max)
    totalGuesses = totalGuesses + numGuesses
    totalGames += 1
    if(bestGuess == 0):
        bestGuess = numGuesses
    elif(numGuesses < bestGuess):
        bestGuess = numGuesses
    playing = playAgain()

results(totalGuesses, totalGames, bestGuess)