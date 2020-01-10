
board = [' ']*9

from os import system, name
# define our clear function
def screen_clear():
    _ = system('clear')

def display_board():
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')

def checkBoard():
    if (board[0], board[1], board[2]) == ('X', 'X', 'X') or (board[3], board[4], board[5]) == ('X', 'X', 'X') or (board[6], board[7], board[8]) == ('X', 'X', 'X') or (board[0], board[3], board[6]) == ('X', 'X', 'X') or (board[1], board[4], board[7]) == ('X', 'X', 'X') or (board[2], board[5], board[8]) == ('X', 'X', 'X') or (board[0], board[4], board[8]) == ('X', 'X', 'X') or (board[2], board[4], board[6]) == ('X', 'X', 'X'):
        print('Player-1 wins')
        return 1
    elif (board[0], board[1], board[2]) == ('O', 'O', 'O') or (board[3], board[4], board[5]) == ('O', 'O', 'O') or (board[6], board[7], board[8]) == ('O', 'O', 'O') or (board[0], board[3], board[6]) == ('O', 'O', 'O') or (board[1], board[4], board[7]) == ('O', 'O', 'O') or (board[2], board[5], board[8]) == ('O', 'O', 'O') or (board[0], board[4], board[8]) == ('O', 'O', 'O') or (board[2], board[4], board[6]) == ('O', 'O', 'O'):
        print('Player-2 wins')
        return 1
    elif ' ' not in board:
        print('Draw')
        return 1

screen_clear()
while True:
    while(True):
        try:
            board_position = int(input("Player-1: Please enter a number for the board position choice: "))
            if board[board_position-1] == ' ':
                board[board_position-1] = "X"
                break
            else:
                print("Kindly please check the board position you entered is already filled.")
        except:
            print("Please enter a number for board position within 1-9")

    screen_clear()
    display_board()
    if checkBoard()==1:
        break

    while(True):
        try:
            board_position = int(input("Player-2: Please enter a number for the board position choice: "))
            if board[board_position-1] == ' ':
                board[board_position-1] = "O"
                break
            else:
                print("Kindly please check the board position you entered is already filled.")
        except:
            print("Please enter a number for board position within 1-9")

    screen_clear()
    display_board()
    if checkBoard()==1:
        break
