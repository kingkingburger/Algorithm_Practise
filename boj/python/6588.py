import sys
import time

a = [False, False] + [True] * (1000000)

#에라토스테네스의 체로 리스트a를 조정한다.
for i in range(2, 1000000):
    if(a[i]):
        for j in range(i*2, 1000000, i):
            a[j] = False
#여기서 리스트 a는 소수만 True

#소수를 구하는 함수
def prime_num(n):
    for i in range(3, n):
        #소수라면
        if(a[i]):
            if((a[n - i]) and ((n-i)%2 != 0)):
                print(n,"=",i,"+",n - i)
                return
    #두 홀수 소수의 합으로 n을 나타낼 수 없는 경우 
    print("Goldbach's conjecture is wrong.")


#0이 입력되기 전까지 while문 돈다.
test_case = int(sys.stdin.readline())
while(test_case != 0):
    
    prime_num(test_case)
       
    test_case = int(sys.stdin.readline())
    