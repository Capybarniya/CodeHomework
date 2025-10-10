

def code(s, shift):
    
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'

    res = ''
    
    if s in rus_alph:
        for e in s:
            i = rus_alph.find(e) + shift
            i = i - (i > len(rus_alph))*len(rus_alph)*(i//len(rus_alph))
            res += rus_alph[i]
        return res 
    else:
        for e in s:
            i = eng_alph.find(e) + shift
            i = i - (i > len(eng_alph))*len(eng_alph)*(i//len(eng_alph))
            res += eng_alph[i]
        return res 

def encode(s,shift):

    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'

    res = ''
    
    if s in rus_alph:
        for e in s:
            i = rus_alph.find(e) - shift
            i = i - (i > len(rus_alph))*len(rus_alph)*(i//len(rus_alph))
            res += rus_alph[i]
        return res 
    else:
        for e in s:
            i = eng_alph.find(e) - shift
            i = i - (i > len(eng_alph))*len(eng_alph)*(i//len(eng_alph))
            res += eng_alph[i]
        return res

op_type = input('Введите тип операции(1 - Шифр/2 - Дешифр): ')
s, shift = input('Введите строку и сдвиг: ').split()
shift = int(shift)
if op_type == '1': print(code(s, shift))
else: print(encode(s, shift))






    
