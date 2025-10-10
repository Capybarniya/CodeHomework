str_in = input()

glas = "аеёиоуыэюя"
soglas = "бвгджзйклмнпрстфхцчшщ"

c_glas, c_soglas = 0, 0
letters_freq = {x : 0 for x in glas+soglas}

for e in str_in:
    if e in glas: 
        c_glas += 1
        letters_freq[e] = letters_freq[e] + 1
    elif e in soglas: 
        c_soglas += 1
        letters_freq[e] = letters_freq[e] + 1
        
freq_out = sorted(list(letters_freq.items()), key = lambda x: x[1])[-3:][::-1]     
print(f"""Количество согласных: {c_soglas}
Количество гласных: {c_glas}
Количество пробелов: {str_in.count(' ')}
Самые частые символы: 
{freq_out[0][0]} - {freq_out[0][1]}
{freq_out[1][0]} - {freq_out[1][1]}
{freq_out[2][0]} - {freq_out[2][1]}
Количество слов: {len(str_in.split())}""")

print()