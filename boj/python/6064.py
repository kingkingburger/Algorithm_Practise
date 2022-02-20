E, S, M = map(int,input().split())

count_E = 0
count_S = 0
count_M = 0

for i in range(1,40000+1):
    count_E += 1
    count_S += 1
    count_M += 1
    if((count_E % 16) == 0):
        count_E = 1
    if((count_S % 29) == 0):
        count_S = 1
    if((count_M % 20) == 0):
        count_M = 1
    if(count_E == E and count_S == S and count_M == M):
        print(i)
        break

        