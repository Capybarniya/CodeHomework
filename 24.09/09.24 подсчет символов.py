str_in = input()
amounts_dict = dict()

print('Кол-во символов')

for i in set(str_in):
    print(f'{i} = {str_in.count(i)}')
    amounts_dict[i] = str_in.count(i)
    
print('Максимальные кол-во')

max_amounts = sorted(list(amounts_dict.items()), key= lambda x: x[1])[-3:][::-1]
for i in range(len(max_amounts)):
    print(max_amounts[i][0], '=', max_amounts[i][1])


