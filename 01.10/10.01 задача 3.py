def print_pack_report(cakes):
    for i in range(cakes,0,-1):
        if not i % 3 and not i % 5: print(f'{i} - расфасуем по 3 или по 5')
        elif not i % 5: print(f'{i} - расфасуем по 5')
        elif not i % 3: print(f'{i} - расфасуем по 3')
        else: print(f'{i} - не заказываем!!')

print_pack_report(int(input('Введите колличество пироженных: ')))
