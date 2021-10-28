import math
num = int(input())

# 에라토스테네스의 체로 소수 구하기
# sosu_nums = []
# a = [False, False] + [True]*(num-1)


# for i in range(2,num+1):
#     if(a[i]):
#         sosu_nums.append(i)
#         for j in range(2*i, num+1, i):
#             a[j] = False

# 일반적인 소수구하기, 제곱근으로 소수 구하기
# for i in range(1,num+1):
#     count = 0
#     if(i > 1):
#         for j in range(2, int(math.sqrt(i)+1)):
#             #소수가 아님을 판별
#             if(i % j == 0):
#                 count +=1
#                 break    
#         if(count == 0):
#             sosu_nums.append(i)

t = 2
while(num >= 0):
    if(num == 1):
        break
    
    #들어온 값이 2부터 나눠진다면
    if((num) % t == 0):
        print(t)
        num = num // t
        t = 2
        continue
    t += 1
    


    
