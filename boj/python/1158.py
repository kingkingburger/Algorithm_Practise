n, k = map(int, input().split())

li = [i for i in range(1,n+1)]

point = li.index(k)
numerical = []

#li가 빌 때까지 한다.
while(len(li)):
    #해당 값을 꺼낸다.
    result = li.pop(point)
    numerical.append(str(result))

    #li가 비어있다면 탈출
    if(len(li) == 0):
        break
    else:
        #k-1은 인덱스가 0부터 시작하기 때문
        point = (point + (k-1)) % len(li)


print("<",", ".join(numerical),">", sep='')
