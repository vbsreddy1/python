player1count = 0
player2count = 0
totalcount = 0

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
        print(f'{player1} wins')
        print(player1count)
        player1count = player1count+1
        totalcount = totalcount+1
        return 1
    elif (board[0], board[1], board[2]) == ('O', 'O', 'O') or (board[3], board[4], board[5]) == ('O', 'O', 'O') or (board[6], board[7], board[8]) == ('O', 'O', 'O') or (board[0], board[3], board[6]) == ('O', 'O', 'O') or (board[1], board[4], board[7]) == ('O', 'O', 'O') or (board[2], board[5], board[8]) == ('O', 'O', 'O') or (board[0], board[4], board[8]) == ('O', 'O', 'O') or (board[2], board[4], board[6]) == ('O', 'O', 'O'):
        print(f'{player2} wins')
        player2count = player2count+1
        totalcount = totalcount+1
        return 1
    elif ' ' not in board:
        print('Draw')
        totalcount = totalcount+1
        return 1

def game(playername,playernum, board):
    mark = ' '
    while(True):
        try:
            board_position = int(input(f"{playername}: Please enter a number for the board position choice: "))
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


screen_clear()
player1 = input("Enter Player-1 Name:")
player2 = input("Enter Player-2 Name:")
print(f'{player1} symbol ******* X \n{player2} symbol ------- O')

while True:
    board = [' ']*9
    display_board(board)
    while True:
        board = game(player1, 1, board)
        screen_clear()
        display_board(board)
        if checkBoard(board)==1:
            break

        board = game(player2, 2, board)

        screen_clear()
        display_board(board)
        if checkBoard(board)==1:
            break

    replay = input("Do you want replay the game(yes/no):")
    replay = replay.upper()
    if replay != 'YES' and replay != 'Y':
        break
    screen_clear()

drawmatches = totalcount - (player1count+player2count)
print(f"Total Matches Played:{totalcount}")
print(f"{player1} won: {player1count}")
print(f"{player2} won: {player2count}")
print(f"Draw matches: {drawmatches}")
