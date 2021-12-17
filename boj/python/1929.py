m,n = map(int, input().split())
count = 0
a = [False, False] + [True] * (n-1)

#에라토스테네스의 체로 리스트a를 조정한다.
for i in range(2, n+1):
    if(a[i]):
        
        for j in range(i*2, n +1, i):
            a[j] = False

#리스트a가 True일 때 인덱스를 출력
for i in range(m, n+1):  
    if(a[i]):
        print(i)