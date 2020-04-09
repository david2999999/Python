from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker
    player2 = 'X' if player1 == 'O' else 'O'

    return player1, player2

player1_marker, player2_marker = player_input()