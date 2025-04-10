print ('Добро пожаловать в игру "Крестики_нолики"')

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def draw_board(board):
    print ('_'* 13)
    for  i in range (3):
            print('|', board[0+i *3], '|', board[1+i *3], '|', board[2+i *3], '|')
            print ('_'* 13)

def take_input(simbol):
    flag = False
    while not flag:
        play_ans = input('Куда поставим ' + simbol +'?')
        try:
            play_ans = int(play_ans)
        except ValueError:
            print('Некорректный ввод!')
            continue
        if 1 <= play_ans <= 9:
            if str(board[play_ans - 1]) not in 'X0':
                board[play_ans - 1] = simbol
                flag = True
            else:
                print('"Эта клетка занята')
        else:
            print('Некорректный ввод. Выберите число от 1 до 9')

def chek_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for ind in win_coord:
        if board[ind[0]] == board[ind[1]] == board[ind[2]]:
            return board [ind[0]]
    return False
def main(board):
    count = 0
    flag = False
    while not flag:
        draw_board(board)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input ('0')
        count += 1
        tmp = chek_win(board)
        if tmp:
            print(tmp,'Выйграл!')
            flag = True
            break
        if count == 9:
            print ('Ничья!')
    draw_board(board)
main(board)