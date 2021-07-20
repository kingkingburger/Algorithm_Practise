
def add(n):
    
    if(n<0):
        return 0
    if(n==1):
        return 1
    elif(n==2):
        return 2
    elif(n==3):
        return 4

    return add(n-1)+add(n-2)+add(n-3)
num=int(input())
for _ in range(num):
    act_num = int(input())
    print(add(act_num))