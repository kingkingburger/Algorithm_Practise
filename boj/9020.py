#소수를 구하는 함수
def prime_num(n):
    a = [False, False] + [True] * (n-1)
    b = []

    #에라토스테네스의 체로 리스트a를 조정한다.
    for i in range(2, n+1):
        if(a[i]):
            for j in range(i*2, n +1, i):
                a[j] = False

    
    for i in range(n//2,n+1):  
        #소수라면
        if(a[i]):
            if(a[n - i]):
                print(n-i, i)
                return

#입력받은 만큼만 while문 돈다.
case = int(input())
while(case > 0):
    test_case = int(input())

    prime_num(test_case)
    case -= 1

    
