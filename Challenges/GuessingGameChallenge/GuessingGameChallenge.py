__author__ = 'VBSREDDY'
__date__ = '30/11/2019'

from random import randint
randomInt = randint(1,100)
count = 0
previousGuess = []
while(True):
    a = int(input("Guess the number:"))
    if a<1 or a>100:
        print('OUT OF BOUNDS')
        continue
    elif a== randomInt:
        print("Congrats! You have guessed the number correctly.")
        print(f'You have taken {count} guesses.')
        break
    elif count==0:
        if abs(a-randomInt) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        # if the previous guessed number is farther away from random-integer than current guessed number, if-block will execute.
        if abs(previousGuess[-1]-randomInt) >= abs(a-randomInt):
            print('WARMER!')
        else:
            print('Farther!')
    count +=1
    previousGuess.append(a)
