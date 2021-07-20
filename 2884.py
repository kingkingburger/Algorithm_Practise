h,m = map(int, input().split(' '))
m += 15
h -= 1
print(m)
if(m == 60 or 65 or 70 or 75):
    m = m - 45
if(h <0):
    h = 23

print(h, m)


