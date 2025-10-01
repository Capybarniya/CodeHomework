from random import randint, choices, shuffle

nums, alpha, spec, upper_alpha = '0123456789', 'abcdefghijklmnopqrstuvwxyz', '_-/()', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

length = int(input('Введите длину пароля: '))
is_alpha = int(input('Нужны буквы? (1/0): '))
is_nums = int(input('Нужны цифры? (1/0): '))
is_spec = int(input('Нужны специальный символы? (1/0): '))
is_upper_alpha = int(input('Нужны большие буквы? (1/0): '))

ises = (is_nums, is_alpha, is_spec, is_upper_alpha)


if sum(ises) == 0:
    print('Слишком мало условий!')
elif sum(ises) < length:
    len_nums, len_alpha, len_spec, len_upper_alpha = 0, 0, 0, 0
    lens = []
    if is_nums:
        len_nums = randint(1,length-(sum(ises)-len(lens)+sum(lens))+1)
        lens += [len_nums]
    if is_alpha:
        len_alpha = randint(1,length-(sum(ises)-len(lens)+sum(lens))+1)
        lens += [len_alpha]
    if is_spec:
        len_spec = randint(1,length-(sum(ises)-len(lens)+sum(lens))+1)
        lens += [len_spec]
    if is_upper_alpha:
        len_upper_alpha = randint(1,length-(sum(ises)-len(lens)+sum(lens))+1)
        lens += [len_upper_alpha]
    #print(lens)
    password = list(''.join(choices(nums,k=len_nums))+''.join(choices(alpha,k=len_alpha))+''.join(choices(spec,k=len_spec))+''.join(choices(upper_alpha,k=len_upper_alpha)))
    shuffle(password)
    print(f'Ваш пароль - {"".join(password)}')
else:
    print('Слишком много условий для такого маленького пароля!')
