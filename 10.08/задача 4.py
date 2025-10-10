from random import choice

def init_acc():
    #global accounts
    acc_number = ''.join([choice('1234567890') for _ in range(4)])
    accounts[acc_number] = 0
    print(f'Создан новый счет!\nНомер счёта: {acc_number}')

def show_accs():
    #global accounts
    print('Вот активные счета:')
    for e in accounts:
        print(e, '-', accounts[e], 'рублей')

def top_up_acc():
    #global accounts
    acc = input('Введите номер счета: ')
    amount = int(input('Введите сумму пополнения: '))
    accounts[acc] += amount 
    print(acc, '-', accounts[acc], 'рублей')

def write_off_acc():
    acc = input('Введите номер счета: ')
    amount = int(input('Введите сумму списания: '))
    if accounts[acc] - amount  >= 0:
        accounts[acc] -= amount 
        print(acc, '-', accounts[acc], 'рублей')
    else: print('На счету недостаточно средств!')

def transfer_acc():
    acc_out = input('Введите номер счета cписания: ')
    acc_in = input('Введите номер счета пополнения: ')
    amount = int(input('Введите сумму перевода: '))
    if accounts[acc_out] - amount  >= 0:
        accounts[acc_out] -= amount 
        accounts[acc_in] += amount
        print(acc_in, '-', accounts[acc_in], 'рублей')
        print(acc_out, '-', accounts[acc_out], 'рублей')
    else: print('На счету списания недостаточно средств!')


accounts = dict()

while 1:
    action = input('''\
Выберите действие:
0 - Закрыть программу
1 - Создать новый счет
2 - Просмотреть активные счета
3 - Пополнить счет
4 - Списать со счета
5 - Перевести с одного счета на другой
''')
    match action:
        case '0': break
        case '1': init_acc()
        case '2': show_accs()
        case '3': top_up_acc()
        case '4': write_off_acc()
        case '5': transfer_acc()
        