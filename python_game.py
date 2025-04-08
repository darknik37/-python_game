map = [0,1,2,
       3,4,5,
       6,7,8]
victory = [[0,1,2],
           [3,4,5],
           [6,7,8]]

def print_map():
    print(map [0], end = '')
    print(map [1], end = '')
    print(map [2])

    print(map [3], end = '')
    print(map [4], end = '')
    print(map [5])

    print(map [6], end = '')
    print(map [7], end = '')
    print(map [8])

def step_map(step,symbol):
        map [ind] = symbol

def get_result():
    win = ''

    for i in victory:
        if map [i[0]] =="X" and map [i[1]] =="X" and map [i[2]] =="X":
            win = 'X'
        if map[i[0]] == "0" and map[i[1]] == "0" and map[i[2]] == "0":
            win ='0'

    return win

#Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1 Показываем карту
    print_map()
# Спросим у играющего куда делать ход
if player1 == True:
    symbol = 'X'
    step = int (input('Человек 1, ваш ход'))
else:
    symbol = '0'
    step = int (input('Человек 2, ваш ход'))

    step_map(step,symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

        player1 = not (player1)

    print_map()
    print ("Победил", win)