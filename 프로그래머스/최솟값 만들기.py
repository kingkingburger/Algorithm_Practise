def solution(A,B):
    answer = 0
    aa = sorted(A)
    bb = sorted(B)
    print(aa, bb)
    
    for i in aa:
        answer += (i * bb.pop())

    return answer