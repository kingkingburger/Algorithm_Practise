list_size = int(input())

list = input().split()

stack = []

for i in range(list_size): # 수열의 크기만큼 

    #처음에 스택이 비어있다면 하나 넣고 시작
    if(stack == []):
        stack.append(i)
        continue

    # 스택이 비어있지않거나 해당 인덱스가 높다면 실행
    while(stack != [] and int(list[i]) > int(list[stack[-1]]) ): 
        list[stack.pop()] = list[i]
    stack.append(i)

#남아있는 스택이 있으면 해당 인덱스를 -1로 변환
while(stack != []):
    list[stack.pop()] = -1

#list의 int를 str로 변환
for z in range(len(list)):
    list[z] = str(list[z])

print(' '.join(list)) 

