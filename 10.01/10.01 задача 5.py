

def romanian_out():
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

def romanian_in():
    symbols = 'IVXLCDM'
    values = [1,5,10,50,100,500,1000]
    values_repetable = [1,0,10,0,100,0,1000]

    goal = int(input())

    sym = ''
    val_sum = 0
    i = 0
    start = 0
    while 1:
        if goal > values[i]:
            start = values[i]
        else:
            break

    










    
