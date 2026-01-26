import random
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7), (2,5,8),(0,4,8),(2,4,6)]
board = [' ' for _ in range(9)]
def check_wins(s):
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == s:
            return True
        return False

def is_draw():
    return ' ' not in board

def print_board():
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print(f'{board[6]}|{board[7]}|{board[8]}')

def computer_move():
    empty_cells = [i for i in range(9) if board[i] == ' ']
    if not empty_cells:
        return
    move = random.choice(empty_cells)
    board[move] = 'O'

def tic_tac_toe():
    while True:
        print_board()
        move = int(input('Ход(0-9): '))
        if move<0 and move>8 or board[move] != ' ':
            print('НЕВЕРНО')
            print_board()
            continue
        
        board[move] = 'X'
        if check_wins('X'):
            print('ПОБЕДА')
            print_board()
            break

        if is_draw():
            print('НИЧЬЯ')
            print_board()
            break
        
        computer_move()
        
        if check_wins('O'):
            print('ПОРАЖЕНИЕ')
            print_board()
            break

        if is_draw():
            print('НИЧЬЯ')
            print_board()
            break
tic_tac_toe()