__author__ = 'VBSREDDY'
__date__ = '30/11/2019'

from random import randint
randomInt = randint(1,100)
print(randomInt)
count = 0
previousGuess = []
while(True):
    a = int(input("Guess the number:"))
    previousGuess.append(a)
    print(previousGuess)
    
    if a== randomInt:
        print("Congrats! You have guessed the number correctly.:-)")
        print(f'You have taken {count} guesses.')
        break
    elif count==0:
        if abs(a-randomInt) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(previousGuess[-1]-randomInt) <= abs(a-randomInt) and abs(previousGuess[-1]-randomInt)<=10:
            print('WARMER!')
        else:
            print('Farther!')
    count +=1

