def solution(n, lost, reserve):
    li = sorted(lost)
    l = sorted(lost)
    r = sorted(reserve)
    for i in li:
        if i in reserve:
            l.remove(i)
            r.remove(i)

    for i in l:
        if (i-1) in r:
            r.remove(i-1)
        elif (i+1) in r:
            r.remove(i+1)
        else:
            n -= 1
            
    return n