N = int(input())
erat_list = list(range(2,N))

j = erat_list[0]
k = 0
while j**2 < N:
    i = k
    while i + j < len(erat_list):
        i += j
        erat_list.pop(i)
        i -= 1
    #print(j,erat_list)
    k += 1
    j = erat_list[k]

print(erat_list)
