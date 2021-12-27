import sys

text = list(sys.stdin.readline().rstrip())


flag = False # 정상 출력은 True
result = ''
stack = ''

#< ,' ' 만나기 전에는 전부다 스택에다가 넣어두고
#< 만나면 다른 스택에다가 넣어두고 
#> 만나면 스택이랑 합치면 된다.

for i in text:
    #뒤집어서 출력
    if flag == False:
        if i == '<':
            flag = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
            stack = ''
        else:
            stack = i + stack

    #정상적으로 출력    
    elif flag == True:
        stack += i
        if i == '>':
            flag = False
            result += stack
            stack = ''

print(result + stack)
    


