def solution(num):
    answer = 0
    for i in range(501):

        if(num % 2 == 0):
            num = num // 2
        elif(num %2 != 0):
            num = (num*3) + 1

        if(i == 500 ):
            answer = -1
            break
        if(num == 1):
            answer = i + 1 
            break

    return answer