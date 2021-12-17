import math
test_case = int(input())
num=[test_case]
count = 0

num=list(map(int,input().split()))
def prime_num(n):
    if(n == 1):
        return False
    for j in range(2, int(math.sqrt(n)+1)): #제곱근 까지만 돌기
        if(n % j == 0):
            return False
    return True

for i in num:
    if(prime_num(i)):
        count +=1

print(count)
