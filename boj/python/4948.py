#소수를 구하는 함수
def prime_num(m,n):
    count = 0
    a = [False, False] + [True] * (n-1)

    #에라토스테네스의 체로 리스트a를 조정한다.
    for i in range(2, n+1):
        if(a[i]):
            for j in range(i*2, n +1, i):
                a[j] = False

    #리스트a가 True일 때 인덱스를 출력
    for i in range(m+1, n+1):  
        if(a[i]):
            count += 1
    return count

while(True):
    test_case = int(input())
    #0을 입력하면 종료
    if(test_case == 0):
        break

    count = 0
    count = prime_num(test_case, (test_case*2))
    print(count)
