import sys

test_case = int(sys.stdin.readline())
list = []
value = 1
result = []
for i in range(1,test_case+1):
    
    num = int(sys.stdin.readline())

    for j in range(value ,num+1):
        list.append(j)
        result.append("+")
        value = num+1

    if(list[-1] == num):
        list.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
        
for j in result:
    print(j)