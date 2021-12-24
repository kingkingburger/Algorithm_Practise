n, k = map(int, input().split())

li = [i for i in range(1,n+1)]

point = li.index(k)
numerical = []

while(len(li)):
    result = li.pop(point)
    numerical.append(str(result))

    if(len(li) == 0):
        break
    else:
        point = (point + (k-1)) % len(li)


print("<",", ".join(numerical),">", sep='')
