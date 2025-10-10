from random import shuffle, sample, randrange

length = int(input('Выберите длину пароля: '))

try:
    num_len = randrange(1, length - 2)
    str_len = randrange(1, length - 1 - num_len)
    spe_len = length - num_len - str_len
    
    #print(num_len,str_len,spe_len)
    
    password =  sample('0123456789',num_len) + sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',str_len) + sample('!@#$%^&*',spe_len)
    shuffle(password)

    print(''.join(password))
    
except ValueError:
    print('Длина должна быть больше 3!')
