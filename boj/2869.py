import math
a,b,v=map(int,input().split())

d = a-b

result = ((v-a)/d)+1
print(math.ceil(result))