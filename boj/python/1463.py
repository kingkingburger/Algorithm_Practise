num = int(input())
d = [0] * (num+1)

for i in range(2,num+1):
    #1을 뺀값 보다 작은게 없다면 뺀값이 그 숫자의 최선이다.
    d[i] = d[i-1] + 1 
    if(i % 2 == 0): #2로 나누어 질 때
        d[i] = min(d[i],d[i//2]+ 1) #ai = min(ai-1, a를 2로나눴을때) 검사
    if(i % 3 == 0): #3으로 나누어 질 때
        d[i] = min(d[i],d[i//3]+ 1) #ai = min(ai-1, a를 2로나눴을때 , a를 3로나눴을때) 검사

print(d[num])