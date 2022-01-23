N,S = map(int,input().split())
children = list(map(int,input().split()))
li = []
result = 0
def 최대공약수(num1, num2):
    #num1이 num2보다 크게
    if(num1 < num2):
        a = num1
        num1 = num2
        num2 = a

    while((num1 % num2 != 0)):
        temp = num2
        num2 = (num1 % num2)
        num1 = temp

    return num2

for i in range(N):
    li.append(abs(children[i] - S))

result = li[0]
for j in range(1,len(li)):
    result = 최대공약수(result,li[j])
    
print(result)