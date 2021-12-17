t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    #h = 세로, w = 가로, n = 몇 번째 손님
    if(n % h):
        floor = n % h
    else:
        floor = h

    if(n % h):
        room = (n//h) + 1
    else:
        room = (n//h)

    if(room >= 10 ):
        print("%d%d" % (floor, room))
    else:
        print("%d%02d" % (floor, room))
