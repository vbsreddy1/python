

from os import system, name
# define our clear function
def screen_clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        _ = system('clear')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def display_board(board):
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

def checkBoard(board):
    if (board[0], board[1], board[2]) == ('X', 'X', 'X') or (board[3], board[4], board[5]) == ('X', 'X', 'X') or (board[6], board[7], board[8]) == ('X', 'X', 'X') or (board[0], board[3], board[6]) == ('X', 'X', 'X') or (board[1], board[4], board[7]) == ('X', 'X', 'X') or (board[2], board[5], board[8]) == ('X', 'X', 'X') or (board[0], board[4], board[8]) == ('X', 'X', 'X') or (board[2], board[4], board[6]) == ('X', 'X', 'X'):
        print('Player-1 wins')
        return 1
    elif (board[0], board[1], board[2]) == ('O', 'O', 'O') or (board[3], board[4], board[5]) == ('O', 'O', 'O') or (board[6], board[7], board[8]) == ('O', 'O', 'O') or (board[0], board[3], board[6]) == ('O', 'O', 'O') or (board[1], board[4], board[7]) == ('O', 'O', 'O') or (board[2], board[5], board[8]) == ('O', 'O', 'O') or (board[0], board[4], board[8]) == ('O', 'O', 'O') or (board[2], board[4], board[6]) == ('O', 'O', 'O'):
        print('Player-2 wins')
        return 1
    elif ' ' not in board:
        print('Draw')
        return 1

def game(playernum, board):
    mark = ' '
    while(True):
        try:
            board_position = int(input(f"Player-{playernum}: Please enter a number for the board position choice: "))
            if playernum == 1:
                mark = "X"
            else:
                mark = "O"
            if board[board_position-1] == ' ':
                board[board_position-1] = mark
                return board
            else:
                print("Kindly please check the board position you entered is already filled.")
        except:
            print("Please enter a number for board position within 1-9")



while True:
    board = [' ']*9
    screen_clear()
    print('Player-1 symbol ******* X \nPlayer-2 symbol ------- O')
    display_board(board)
    while True:
        board = game(1, board)
        screen_clear()
        display_board(board)
        if checkBoard(board)==1:
            break

        board = game(2, board)

        screen_clear()
        display_board(board)
        if checkBoard(board)==1:
            break

    replay = input("Do you want replay the game(yes/no):")
    replay = replay.upper()
    if replay != 'YES' and replay != 'Y':
        break
