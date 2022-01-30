d = [0] * (1001)

d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4,1001):
    d[i] = d[i-1] + d[i-2] + d[i-3]

num=int(input())
for _ in range(num):
    act_num = int(input())
    print(d[act_num])