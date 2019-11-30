__author__ = 'VBSREDDY'
__date__ = '30/11/2019'

from random import randint
randomInt = randint(1,100)
count = 0
previousGuess = [0]
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
while(True):
    guess = int(input("Guess the number:"))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS')
        continue
    elif guess == randomInt:
        print("Congrats! You have guessed the number correctly.")
        print(f'You have taken {len(previousGuess)} guesse(s).')
        break
    elif len(previousGuess) < 2:
        if abs(guess-randomInt) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        # if the previous guessed number is farther away from random-integer than current guessed number, if-block will execute.
        if abs(previousGuess[-1]-randomInt) >= abs(guess-randomInt):
            print('WARMER!')
        else:
            print('COLDER!')
    previousGuess.append(guess)
