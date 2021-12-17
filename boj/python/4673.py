not_self_number=[]
x = range(1,10001) #10001까지 리스트
print(type(x))
for i in x: #1~10001까지
    l = list(map(int,str(i)))
    
    #셀프넘버가 아닌 것들
    not_self_number.append(i + sum(l))

for j in x: #1~10001까지
    if j not in not_self_number:
        print(j)
