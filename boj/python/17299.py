from collections import Counter
list_size = int(input())

list = list(map(int,input().split()))

#수열들의 등장 횟수 체크
count = Counter(list)

stack = []

for i in range(list_size): # 수열의 크기만큼 

    #처음에 스택이 비어있다면 하나 넣고 시작
    if(stack == []):
        stack.append(i)
        continue

    #왼쪽 값의 등장 횟수가 오른쪽 보다 작으면 
    while(stack != [] and count[list[stack[-1]]] < count[list[i]] ):
        #왼쪽 값의 오등큰수는 오른쪽 값이다.
        list[stack.pop()] = list[i]

    stack.append(i)

while(stack != []):
    list[stack.pop()] = -1

#list의 int를 str로 변환
for z in range(len(list)):
    list[z] = str(list[z])

print(' '.join(list))

