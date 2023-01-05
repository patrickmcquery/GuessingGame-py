from random import randint
def intro(max):
    print('This program allows you to play a guessing game.')
    print('I will think of a number between 1 and')
    print(max, ' and will allow you to guess until')
    print('you get it. For each guess, I will tell you')
    print('whether the right answer is higher or lower')
    print('than your guess.')

def play(max):
    answer = randint(1, max)
    pnumGuesses = 1
    guessing = True
    while(guessing):
        guess = 0
        typing = True
        while(typing):
            gues = input('Your guess? ')
            guess = int(gues)
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

def results(totGuesses, totGames, bestGuess):
    avg = totGuesses / totGames
    print('Overall results: ')
    print('    total games = ', totGames)
    print('    total guesses = ', totGuesses)
    print('    guess/game = ', avg)
    print('    best game = ', bestGuess)

def playAgain():
    while(True):
        response = input('Do you want to play again? ').lower()[0]
        if(response == "y"):
            return True
        elif(response == "n"):
            return False
        else:
            print('Please enter a valid response.')

max = 100
totalGuesses = 0
totalGames = 0
bestGuess = 0
playing = True

intro(max)

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