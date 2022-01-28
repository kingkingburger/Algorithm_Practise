num = int(input())
d = [0] * (num+1)

if num <= 3:
    print(num)
else:
    d[1] = 1
    d[2] = 2
    for i in range(3,num+1):
        d[i] = d[i-1] + d[i-2] 
    print(d[num] % 10007)