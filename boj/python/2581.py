m = int(input())
n= int(input())
num =[]

for i in range(m, n + 1):
    error =0
    if(i > 1):
        for j in range(2, i):
            #2부터 들어온 값까지 
            if(i % j == 0):
                error += 1
                break
        if(error == 0):
            num.append(i)
if(len(num) >0):
    print(sum(num))
    print(min(num))
else:
    print(-1)