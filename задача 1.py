from random import randint

goal = randint(0,10)

guess = 0

i = 0

print('Угадайте число от 1 до 10')

while guess != goal and i < 3:
    guess = int(input(f"Осталось {3-i} попыток \n Какая ваша догадка? "))
    if guess > goal:
        print('Заданное число меньше')
    elif guess < goal:
        print('Заданное число больше')
    else:
        print(f'Вы угадали! Правильное число - {goal}')
        break
    if i == 1: print('Заданное число четное' if not goal % 2 else 'Заданное число нечетное')
    i += 15
else:
    print(f'Вы не угадали! Правильное число - {goal}')