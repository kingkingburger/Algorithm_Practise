x,y,w,h = map(int, input().split())
#x의 최소값
if(w - x > x):
    width = x
else:
    width = w-x

#y의 최소값
if(h - y > y):
    height = y
else:
    height = h-y

#x축, y축 중 가장 짧은 것
if(width > height):
    print(height)
else:
    print(width)