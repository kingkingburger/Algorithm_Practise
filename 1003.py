
# def fibonacci(n):
#     fibo_0 = [1,0]
#     fibo_1 = [0,1]
 
#     for i in range(2,n+1):
#         fibo_0.append(fibo_0[i-1] + fibo_0[i-2])
#         fibo_1.append(fibo_1[i-1] + fibo_1[i-2])
    
#     print("%d %d"%(fibo_0[-1],fibo_1[-1]))


for i in range(int(input())):
    
    act_num = int(input())
    fibo_0 = [1,0]
    fibo_1 = [0,1]
 
    for i in range(2,act_num+1):
        fibo_0.append(fibo_0[i-1] + fibo_0[i-2])
        fibo_1.append(fibo_1[i-1] + fibo_1[i-2])
    
    if act_num == 0:
        print("%d %d"%(fibo_0[-2],fibo_1[-2]))
    else:
        print("%d %d"%(fibo_0[-1],fibo_1[-1]))
