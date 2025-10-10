from random import choice

score_player, score_prog = 0, 0

turns = ['камень','ножницы','бумага']
print(turns)
while score_player < 3 and score_prog < 3:
    turn_player = input('Ваш ход: ')
    turn_prog = choice(turns)
    #print(turns.index(turn_player) - turns.index(turn_prog))
    print(f'Ход компьютера: {turn_prog}')
    match (turns.index(turn_player) - turns.index(turn_prog)):
        case 0: pass
        case -1: score_player += 1
        case 2: score_player += 1
        case _: score_prog += 1
    print(f'''\
Текущий счет:
Игрок | Компьютер
{score_player}     | {score_prog}\
        ''')
print('ВЫ ВЫЙГРАЛИ!' if score_player == 3 else 'ВЫ ПРОИГРАЛИ!')
    