test_case = int(input())

def stack_empty(str):
    stack = []
    for j in range(len(str)):
        if('(' in str[j]):
            stack.append('(')
            continue
        else:
            try:
                stack.pop()
            except:
                return "NO"
    if(stack == []):
        return "YES"            
    else:
        return "NO"
        

#스택에 '('이 들어오면 넣어줌
# )이 들어오면 뺌 근데 뺄 때 스택에 아무것도 없으면 그건 False

for i in range(test_case):
    str= input()
    print(stack_empty(str))


