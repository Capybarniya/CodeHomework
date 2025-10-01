symbols = 'IVXLCDM'
values = [1,5,10,50,100,500,1000]

s = input()
curr_sum, sum_ = values[symbols.find(s[0])], values[symbols.find(s[0])]

for i in range(1,len(s)):
    val = values[symbols.find(s[i])]
    if val >= values[symbols.find(s[i-1])]:
        sum_ = val - curr_sum
        curr_sum = val

    else:
        curr_sum += val
        sum_ += val
        #print(99)
print(sum_)
