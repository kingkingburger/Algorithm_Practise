import sys
n = int(sys.stdin.readline())
list = []

def com(str):
    if(str[0] == 'push_front'):
        value = str[1]
        list.insert(0, value)
    
    elif(str[0] == 'push_back'):
        value = str[1]
        list.append(value)

    elif(str[0] == 'pop_front'):
        if(len(list)):
            print(list.pop(0))
        else:
            print(-1)

    elif(str[0] == 'pop_back'):
        if(len(list)):
            print(list.pop())
        else:
            print(-1)

    elif(str[0] == 'size'):
        print(len(list))

    elif(str[0] == 'empty'):
        if(len(list)):
            print(0)
        else:
            print(1)

    elif(str[0] == 'front'):
        if(len(list)):
            print(list[0])
        else:
            print(-1)

    elif(str[0] == 'back'):
        if(len(list)):
            print(list[-1])
        else:
            print(-1)

for _ in range(n):
    command = sys.stdin.readline().split()
    com(command)