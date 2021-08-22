
def d():
    not_self_number=[]

    for i in range(1,10000):
        l = list(map(int,str(i)))
        
        #셀프넘버가 아닌 것들
        not_self_number.append(i + sum(l))
    t = [x for x in range(1,10000) if x not in not_self_number]
    for i in t:
        print(i)
d()