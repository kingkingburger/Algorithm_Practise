input = list(input())
stack = []
result = 0

for i in range(len(input)):
    
    if(input[i] == '(' ):
        stack.append(input[i])
    elif(input[i] == ')'):
        if(input[i-1] == '('):
            stack.pop()
            result += len(stack)
            continue
        stack.pop()
        result += 1
     
print(result)