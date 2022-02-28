def solution(n, left, right):
    x = 1
    y = 1
    result = 1
    answer = []

    
    for j in range(left, right+1):
        if(j == 0):
            answer.append(1)
            continue
        x = j // n
        y = j % n
        result = max(x,y)+1
        answer.append(result)
    print(answer)
    
    return answer

solution(1,1000000,1000000)